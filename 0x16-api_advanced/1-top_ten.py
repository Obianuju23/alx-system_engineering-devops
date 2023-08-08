#!/usr/bin/python3
"""
function that queries the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """Function that prints 10 first hot posts for a given subreddit"""

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {'User-Agent': 'My Customised User Agent'}
    limits = {"limit": 10}

    response = requests.get(url, headers=headers, params=limits,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
    else:
        for item in response.json().get("data").get("children"):
            print(item.get("data").get("title"))
