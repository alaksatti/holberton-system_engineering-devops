#!/usr/bin/python3
''' Queries the Reddit API '''
from requests import get
url = 'https://www.reddit.com'
headers = {'User-Agent': 'alaksatti'}


def recurse(sr_input, hot_list=[], next_page=None):
    '''recursive function to return list of hot articles'''
    subreddit_page = url + '/r/' + sr_input + '/hot.json'

    if next_page:
        subreddit_page = subreddit_page + '?after=' + next_page

    subreddit = get(subreddit_page, headers=headers, allow_redirects=False)
    if subreddit.status_code != 200:
        return None
    list_elements = subreddit.json().get('data').get('children')
    next_page = subreddit.json().get('data').get('after')

    for e in list_elements:
        e.get('data').get('title').lower().split(' ')
    if next_page:
        return recurse(sr_input, hot_list, next_page)
    return hot_list
