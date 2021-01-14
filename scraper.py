'''
RESOURCS USED:
https://www.makeuseof.com/beautiful-soup-tutorial/
'''

import argparse
import sys
import requests

# EXAMPLE CMD:
# python scraper.py http://kenzie.academy/


def scraper(link):
    '''Scrapes a website for phone numbers, email addresses, links, and images.'''
    req = requests.get(link)


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('link', help='web address URL to scrape')
    return parser


def main(args):
    parser = create_parser()
    args = parser.parse_args(args)
    url = args.link
    return scraper(url)


if __name__ == '__main__':
    main(sys.argv[1:])
