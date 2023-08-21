# Load data

# Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ . 
# As a result, store all comments in chronological order in JSON and dump it to a file.

import requests

comments = requests.get('https://api.pushshift.io/reddit/comment/search/')
print(comments.status_code, comments.reason)
print(comments.json())

# seems the api doesn't work anymore and server returns code 403 "FORBIDDEN"
# skipping this task