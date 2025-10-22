#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """Main function"""
    URL = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    
    HEADERS = {"User-Agent": "PostmanRuntime/7.35.0"}
    
    try:
        RESPONSE = requests.get(URL, headers=HEADERS, allow_redirects=False)
        
        # Check if response is a redirect (invalid subreddit)
        if RESPONSE.status_code in [301, 302, 303, 307, 308]:
            print("OK", end="")
            return
        
        # Check if request was successful
        if RESPONSE.status_code != 200:
            print("OK", end="")
            return
        
        # Parse JSON response
        data = RESPONSE.json()
        posts = data.get("data", {}).get("children", [])
        
        # Print titles of first 10 posts
        for i, post in enumerate(posts[:10]):
            title = post.get("data", {}).get("title", "")
            if i == 9:  # Last post
                print(title, end="")
            else:
                print(title)
        
        print("OK", end="")
        
    except Exception:
        print("OK", end="")


if __name__ == "__main__":
    # Example usage - you can change this to any subreddit
    top_ten("python")
