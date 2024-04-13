#!/usr/bin/python3
""" function that queries the Reddit API and returns
the number of subscribers """
import requests


def number_of_subscribers(subreddit):
    """ function that queries the Reddit API and returns"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyBot/0.1"}  # Set a custom User-Agent

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    else:
        return 0
