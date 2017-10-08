import os
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
from google.cloud import storage
from google.cloud import language

CREDENTIALS = '../credentials/RoverApp-2c2a3600d6d9.json'
ENV_VAR = 'GOOGLE_APPLICATION_CREDENTIALS'
SAMPLE_BUCKET = 'rover1'
SAMPLE_FILE = 'audio-file.flac'
SAMPLE_STRING = 'several tornadoes touched down as a line of severe thunderstorms swept through Colorado on Sunday'
QUERY = 'wikipedia_url'


def make_verbose(before, after):
    """
    :param before: (bool) whether the arguments should be printed before the
        function call
    :param after: (bool) whether the result should be printed after the
        function call
    :return: (func) a decorator which replaces a function which the verbose version
        as specified by its arguments
    """

    def wrapper(func):
        def verbose(*args, **kwargs):
            if before:
                print(*args, **kwargs)
            output = func(*args, **kwargs)
            if after:
                print(output)
            return output
        return verbose
    return wrapper


def main(func):
    """
    :param func: (func) the function to wrap
    :return: (func) a function which only runs if file itself is run
    """

    def wrapped(*args, **kwargs):
        if __name__ == '__main__':
            func()

    return wrapped


def transcribe_gcs(gcs_uri):
    """
    :param gcs_uri: (str) the Google Cloud Storage URI 'gcs://'
    :return: (str) the most likely transcript of the sort audio
    """
    client = speech.SpeechClient()

    audio = types.RecognitionAudio(uri=gcs_uri)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=44100,
        language_code='en-US')

    response = client.recognize(config, audio)
    top_result = response.results[0]
    return str(top_result.alternatives[0].transcript)


def create_gcs(bucket, filename):
    """
    :param blob: (str) the blob for the particular file
    :param filename: (str) the particular filename
    :return: the URI for the GCS file corresponding to the information given
    """
    return 'gs://' + bucket + '/' + filename


def process_audio(bucket_name, filename, user_id):
    """
    :param bucket_name: (str) the name of the bucket the file is in
    :param filename: (str) the filename of the audio clip
    :return: (str) the most likely transcript of the sort audio
    """
    # Derive transcript
    os.environ[ENV_VAR] = CREDENTIALS
    gcs_uri = create_gcs(bucket_name, filename)
    result = transcribe_gcs(gcs_uri)

    # Delete original audio file
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blob = bucket.get_blob(filename)
    blob.delete()

    # Return transcript
    return result


def run_analyses(text):
    """
    :param text: (str) paragraph to be analyzed
    :return: results of important analyses
    """
    client = language.Client()
    document = client.document_from_text(text)
    entities = find_entities(document)
    return entities


def find_entities(text_doc):
    """
    :param text_doc: (document) text to be analyzed
    :return: [(str, str, float, dict)] containing entity, type, salience and
        relevant links for each key word in the sentence
    """
    entity_response = text_doc.analyze_entities()
    key_entities = []
    for entity in entity_response.entities:
        key_entities.append([
            entity.name,
            entity.entity_type,
            entity.salience,
            entity.metadata
        ])
    return key_entities


def terms_and_links(entities, link_type):
    """
    :param entities: [(str, str, float, dict)] containing entity, type, salience and
        relevant links for each key word in the sentence
    :return: ([str], [str]) list consisting of words sorted from most to least relevant,
        containing relevant wikipedia links
    """
    sorted_entities = sorted(entities, key=lambda entity: entity[2], reverse=True)
    words = [entity[0] for entity in sorted_entities]
    links = []
    for entity in sorted_entities:
        if link_type in entity[3]:
            links.append(entity[3][link_type])
    return words, links


@main
def run():
    # output = process_audio(SAMPLE_BUCKET, SAMPLE_FILE, 0)
    os.environ[ENV_VAR] = CREDENTIALS
    output = run_analyses(SAMPLE_STRING)
    print(terms_and_links(output, QUERY))


run()
