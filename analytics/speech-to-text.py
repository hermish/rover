import os; import io
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

CREDENTIALS = '../credentials/RoverApp-2c2a3600d6d9.json'
ENV_VAR = 'GOOGLE_APPLICATION_CREDENTIALS'
URI = 'gs://rover1/audio-file.flac'


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


@make_verbose(False, True)
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


@main
def root():
    os.environ[ENV_VAR] = CREDENTIALS
    transcribe_gcs(URI)


root()