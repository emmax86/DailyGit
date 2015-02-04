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
parser.add_argument("--date", help="Date to analyze")


class RectParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'rect':
            date = attrs[6]
            datestring = ""
            if args.date is None:
                date_today = datetime.now().date()
                datestring = date_today.strftime("%Y-%m-%d")
            else:
                datething = datetime.strptime(args.date, "%Y-%m-%d")
                datestring = datething.strftime("%Y-%m-%d")
            if (date[1] == datestring):
                if attrs[5][1] != "":
                    print attrs[5][1]
                else:
                    print "Could not retrieve amount of commits."

args = parser.parse_args()
response = urllib2.urlopen("https://github.com/{}".format(args.github))
html = response.read()
parser = RectParser()
parser.feed(html)
