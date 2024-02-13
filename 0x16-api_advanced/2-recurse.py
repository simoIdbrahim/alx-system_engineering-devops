#!/usr/bin/python3
""" function that queries the Reddit API and returns a list """
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """ return list of title """
    information = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            params={"count": count, "after": after},
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if information.status_code >= 400:
        return None

    hot = hot_list + [child.get("data").get("title")
                        for child in information.json()
                        .get("data")
                        .get("children")]

    info = information.json()
    if not info.get("data").get("after"):
        return hot

    return recurse(subreddit, hot, info.get("data").get("count"),
                   info.get("data").get("after"))
