#!/usr/bin/python3
"""
Recursive function that queries the Reddit API, parses the title of all hot
articles, and prints a sorted count of given keywords
"""
import requests
from collections import Counter


def count_words(subreddit, word_list, after=None, count=None):
    """Function that count words found in hot posts using REDDIT API
    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        after (str): The parameter for the next page of the API results.
        count (int): The parameter of results matched thus far.
    """

    if count is None:
        count = Counter()
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if after:
        parameters = {"after": after}
    else:
        parameters = {}
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My Customised User Agent 1.0'})
    response = requests.get(url, headers=headers, params=parameters,
                            allow_redirects=False)
    if response.status_code == 200:
        result = response.json()
        hots = result['data']['children']
        for item in hots:
            title = item['data']['title']
            translator = str.maketrans('', '', '.,!?()[]{}"\'')
            words_in_title = [word.translate(translator) for word in
            title.lower().split()]
            lower_word_list = set(w.lower() for w in word_list)
            for word in words_in_title:
                if word in lower_word_list:
                    count[word] += 1

        after = result['data']['after']
        if after:
            return count_words(subreddit, word_list, after, count)
        else:
            sorted_counts = sorted(count.items(), key=lambda x: (-x[1], x[0]))
            for w, c in sorted_counts:
                print("{}: {}".format(w, c))
            return count
    else:
        return None
