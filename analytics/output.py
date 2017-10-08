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


# def return_reddit(parsed, max_results):
#     read_credentials =
#
#
# def read_credentials(file_name):
#     """
#     Reads and return API credentials from a text file.
#     :param file_name: (str) the name of the file which hold this information
#     :return: [str] the client_id, secret and agent
#     """
#     data = open(file_name)
#     information = [line.rstrip() for line in data]
#     return information
#
#
# def scrape_data(client_id, secret, agent, extractor):
#     """
#     Creates and returns a generator which provides a sequence of outputs to be written.
#     :param client_id: (str) client id for the Reddit API
#     :param secret: (str) client secret for the Reddit API
#     :param agent: (str) user agent description
#     :param extractor: function which extracts the desired information from reddit
#     :return: a generator which yields
#     """
#     reddit = praw.Reddit(client_id=client_id,
#                          client_secret=secret,
#                          user_agent=agent)
#     return extractor(reddit)




@main
def test():
    """
    Main method mostly for testing
    :return: None
    """
    pass
