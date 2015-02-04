#!/usr/local/bin/python
import argparse
from datetime import datetime
from HTMLParser import HTMLParser
import urllib2

parser = argparse.ArgumentParser(description="A script for checking a day's \
                                              commits on GitHub.")
parser.add_argument("--github",
                    help="GitHub username of the user you would like to inspect.",
                    required=True)


class RectParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'rect':
            date = attrs[6]
            date_today = datetime.now().date()
            datestring = date_today.strftime("%Y-%m-%d")
            if (date[1] == datestring):
                print attrs[5][1]

args = parser.parse_args()
response = urllib2.urlopen("https://github.com/{}".format(args.github))
html = response.read()
parser = RectParser()
parser.feed(html)
