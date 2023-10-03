#!/usr/bin/python3
"""
Takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import requests
import sys


if __name__ == "__main__":
    api = "https://api.github.com/user"
    response = requests.get(api, auth=(sys.argv[1], sys.argv[2]))
    result = response.json()
    print(result.get("id"))
