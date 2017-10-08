import scholarly


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


@main
def test():
    """
    Main method mostly for testing
    :return: None
    """
    pass
