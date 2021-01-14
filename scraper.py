'''
RESOURCS USED:
https://www.makeuseof.com/beautiful-soup-tutorial/
http://emailregex.com/
'''

import argparse
import sys
import requests
from bs4 import BeautifulSoup, SoupStrainer
import re


def scraper(link):
    website = requests.get(link)
    soup = BeautifulSoup(website.content, 'html.parser')

    image_data = []
    all_links = []

    # IMAGE INFO:
    images = soup.select('img')
    for image in images:
        src = image.get('src')
        alt = image.get('alt')
        image_data.append({'src': src, 'alt': alt})
    print('IMAGE INFO:', '\n', image_data)

    links = soup.select('a')
    for ahref in links:
        href = ahref.get('href')
        href = href.strip() if href is not None else ''
        all_links.append(href)
    print('LINKS:', '\n', all_links)


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
