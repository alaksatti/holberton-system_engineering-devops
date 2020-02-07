#!/usr/bin/python3
''' Queries the reddit API '''
from requests import get

url = 'https://www.reddit.com'
header = {'User-Agent': 'alaksatti'}


def number_of_subscribers(sr_input):
    '''finds the number of subs to this subreddit'''
    sreddit_about = url + '/r/' + sr_input + '/about.json'
    subreddit = get(sreddit_about, headers=header, allow_redirects=False)

    if subreddit.status_code != 200:
        return 0

    return subreddit.json().get('data').get('subscribers')
