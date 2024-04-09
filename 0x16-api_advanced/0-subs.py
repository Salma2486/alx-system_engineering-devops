#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""

import requests

def number_of_subscribers(subreddit):
    # Define the URL of the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set custom User-Agent to avoid "Too Many Requests" error
    headers = {"User-Agent": "custom"}

    try:
        # Make a GET request to the subreddit's about page without following redirects
        response = requests.get(url, headers=headers, allow_redirects=False)

        # If the response status code is 200, parse the JSON and return the subscriber count
        if response.status_code == 200:
            data = response.json()
            return data.get("data", {}).get("subscribers", 0)
        else:
            # If the response status code is not 200, return 0
            return 0
    except Exception as e:
        # If an exception occurs (e.g., network error), return 0
        print(f"Error: {e}")
        return 0
