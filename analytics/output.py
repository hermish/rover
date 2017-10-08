import scholarly
import praw


def main(func):
    """
    :param func: (func) the function to wrap
    :return: (func) a function which only runs if file itself is run
    """
    def wrapped(*args, **kwargs):
        if __name__ == '__main__':
            func()
    return wrapped


def return_scholar(parsed, max_results):
    """
    :param parsed: [str] a list of import words which need to be searched
    :param max_results: (int) number of articles to return
    :return: a list consisting of articles
    """
    raw_query = ' '.join(parsed)
    list_of_articles = []
    search_query = scholarly.search_pubs_query(raw_query)
    for thing in search_query:
        if not max_results:
            break
        summary = thing.fill().bib
        list_of_articles.append([
            summary['title'], summary['author'], summary['abstract'], summary['url']])
        max_results -= 1
    return list_of_articles


def return_reddit(parsed, max_results):
	# TODO: Determine posts to extract
    pass


def read_credentials(file_name):
    """
    Reads and return API credentials from a text file.
    :param file_name: (str) the name of the file which hold this information
    :return: [str] the client_id, secret and agent
    """
    data = open(file_name)
    information = [line.rstrip() for line in data]
    return information


def scrape_data(client_id, secret, agent, extractor):
    """
    Creates and returns a generator which provides a sequence of outputs to be written.
    :param client_id: (str) client id for the Reddit API
    :param secret: (str) client secret for the Reddit API
    :param agent: (str) user agent description
    :param extractor: function which extracts the desired information from reddit
    :return: a generator which yields
    """
    reddit = praw.Reddit(client_id=client_id,
                         client_secret=secret,
                         user_agent=agent)
    return extractor(reddit)


def is_serializable(obj):
    """
    :param obj: object to check
    :return: (bool) whether or not the object can be json serialized
    """
    try:
        json.dumps(obj)
        return True
    except TypeError:
        return False


def change_attributes(dictionary, to_remove, func):
    """
    :param dictionary: (dict)
    :param to_remove: [str] the dictionary keys which have values to be transformed
    :param func: (func) the function to be applied
    :return: (dict) new dictionary with different values, mapping the function
        to the values of the dictionary which are in
    """
    return {key: (func(value) if key in to_remove else value) for
            key, value in dictionary.items()}


def map_to_values(func, dictionary):
    """
    :param func: (function) function to be mapped
    :param dictionary: (dict) the original hash map
    :return: (dict) new dictionary with different values,
        mapping the function to the values of the dictionary
    """
    return {key: func(value) for key, value in dictionary.items()}


def respect_limit(requests):
    """
    :param requests: (int) the current number of
    :return: (int) an updated number of requests, sleeping the required amount of
        time and resetting if an additional call would push the requests over the
        specified limit
    """
    if requests + 1 > API_LIMIT:
        time.sleep(SLEEP_TIME)
        return 1
    return requests + 1


def get_posts(reddit, subreddits, mode, time_filter, num_comments, sub_coerce, com_coerce):
    """
    :param reddit: (reddit) an possibly unauthenticated reddit instance
    :param subreddits: [str] the subreddits to pull data from
    :param mode: (str) the string referring to browsing mode, for example 'rising'
    :param time_filter: (str) the time period for the mode selected
    :param num_comments: (int) the number of comments to select
    :param sub_coerce: [str] list of attributes for submissions to coerce to strings
    :param com_coerce: [str]list of attributes for comments to coerce to strings
    :return: (gen) a generator which returns, at every successive call, list of each
        post and the requested number of top comments until exhaustion
    """
    requests = 1
    for sub in subreddits:
        subreddit = reddit.subreddit(sub)
        post_gen = getattr(subreddit, mode)(time_filter=time_filter)
        requests = respect_limit(requests)
        for submission in post_gen:
            requests = respect_limit(requests)
            output = [change_attributes(vars(submission), sub_coerce, str)]
            comments_left = num_comments
            requests = respect_limit(requests)
            for comment in submission.comments:
                requests = respect_limit(requests)
                if not comments_left:
                    break
                output.append(change_attributes(vars(comment), com_coerce, str))
                comments_left -= 1
            yield output


@main
def test():
    """
    Main method mostly for testing
    :return: None
    """
    pass
