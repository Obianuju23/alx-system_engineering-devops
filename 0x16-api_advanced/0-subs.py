#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Returns total number of subscribers in a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            result = response.json().get("data")
        else
            return 0
        return result.get("subscribers")
