#!/usr/bin/python3
""" functiona function that queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit. """


def top_ten(subreddit):
    """ Queries the Reddit API and returns the top 10 hot posts
    of the subreddit """
    import requests
    info = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                        .format(subreddit),
                        headers={"User-Agent": "MyBot/0.1"})
    if info.status_code == 200:
        for post in info.json().get("data").get("children"):
            print(post.get("data").get("title"))
    else:
        print(None)
