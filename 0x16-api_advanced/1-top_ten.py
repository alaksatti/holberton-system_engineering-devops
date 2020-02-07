#!/usr/bin/python3
''' Queries the reddit API '''
from requests import get
url = 'https://www.reddit.com'
headers = {'User-Agent': 'alaksatti'}


def top_ten(sr_input):
    '''prints the first 10 hotposts for subreddit'''
    subreddit_page = url + '/r/' + sr_input + '/hot.json?limit=10'
    subreddit = get(subreddit_page, headers=headers, allow_redirects=False)
    if subreddit.status_code != 200:
        print('None')

    for list_item in subreddit.json().get('data').get('children'):
        print(list_item.get('data').get('title'))
