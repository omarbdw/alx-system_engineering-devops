#!/usr/bin/python3
"""Module for task 2"""


def recurse(subred, hotList=[], counter=0, after=None):
    """Queries the Reddit API and returns all hot posts
    of the subred"""
    import requests

    subInfo = requests.get("https://www.reddit.com/r/{}/hot.json"
                           .format(subred),
                           params={"counter": counter, "after": after},
                           headers={"User-Agent": "My-User-Agent"},
                           allow_redirects=False)
    if subInfo.status_code >= 400:
        return None

    hot_l = hotList + [child.get("data").get("title")
                       for child in subInfo.json()
                       .get("data")
                       .get("children")]

    info = subInfo.json()
    if not info.get("data").get("after"):
        return hot_l

    return recurse(subred, hot_l, info.get("data").get("counter"),
                   info.get("data").get("after"))
