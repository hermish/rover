from input import process_audio, run_analyses
from output import return_scholar


# MAIN CONSTANTS
CREDENTIALS = '../credentials/RoverApp-2c2a3600d6d9.json'
LINK_TYPE = 'wikipedia_url'
NUM_ARTICLES = 3

# TEST CONSTANTS
SAMPLE_BUCKET = 'rover1'
SAMPLE_FILE3 = 'audio (5).ogg'
SAMPLE_FILE2 = 'audio-file.flac'
SAMPLE_FILE1 = 'sample.flac'


def main(bucket_name, filename, sample_rate, user_id):
    raw_text = process_audio(CREDENTIALS, bucket_name, filename, sample_rate, user_id)
    complete_data = run_analyses(raw_text, LINK_TYPE)
    keywords = complete_data[0]
    list_of_articles = return_scholar(keywords, NUM_ARTICLES)
    return list_of_articles


def test():
    result = main(SAMPLE_BUCKET, SAMPLE_FILE2, 44100, 0)
    return result
