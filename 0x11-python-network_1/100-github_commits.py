#!/usr/bin/python3
"""
Print 10 github commits of a given repo and user
"""

import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    user = sys.argv[2]
    api = "https://api.github.com/repos/{}/{}/commits".format(user, repo)
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    response = requests.get(api, headers=headers)
    commits = response.json()
    for commit in commits[:10]:
        sha = commit.get("sha")
        author = commit.get("commit").get("author").get("name")
        print("{}: {}".format(sha, author))
