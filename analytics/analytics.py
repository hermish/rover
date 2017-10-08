from input import process_audio, run_analyses
from output import return_scholar

# MAIN CONSTANTS
CREDENTIALS = '../credentials/RoverApp-2c2a3600d6d9.json'
LINK_TYPE = 'wikipedia_url'

# TEST CONSTANTS
SAMPLE_BUCKET = 'rover1'
SAMPLE_FILE2 = 'audio-file.flac'
SAMPLE_FILE1 = 'sample.flac'


def main(bucket_name, filename, sample_rate, user_id):
    raw_text = process_audio(CREDENTIALS, bucket_name, filename, sample_rate, user_id)
    result = run_analyses(raw_text, LINK_TYPE)
    return result


def test():
    result = main(SAMPLE_BUCKET, SAMPLE_FILE2, 44100, 0)
    print(result)


test()