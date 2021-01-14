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
    soup_img = BeautifulSoup(
        website.content, 'html.parser', parse_only=SoupStrainer('img'))
    soup = BeautifulSoup(website.content, 'html.parser')
    soup_link = BeautifulSoup(
        website.content, 'html.parser', parse_only=SoupStrainer('a'))

    for link in soup_link:
        if link.has_attr('href'):
            address = link.get('href')
            url = re.search(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                            str(address))
            if url:
                print('URL: ' + url.group())

    for image in soup_img:
        src = image.get('src')
        print('IMAGE: ' + str(src))

    for number in soup:
        numbers = re.search(
            r'1?\W*([2-9][0-8][0-9])\W*([2-9][0-9]{2})\W*([0-9]{4})(\se?x?t?(\d*))?', str(number))
        if numbers:
            print('PHONE NUMBER: ' + numbers.group())

    for email in soup:
        emails = re.search(
            r'([a-zA-Z]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.][a-zA-Z]+)', str(email))
        if emails:
            print('EMAIL: ' + emails.group())


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
