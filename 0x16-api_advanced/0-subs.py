#!/usr/bin/python3
""" Queries the Reddit API and returns the number of subscribers"""


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers for a given subreddit"""
    import requests

    response = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if response.status_code >= 300:
        return 0

    return response.json().get("data").get("subscribers")
