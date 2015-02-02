from datetime import datetime
from HTMLParser import HTMLParser
import urllib2


class RectParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'rect':
            date = attrs[6]
            date_today = datetime.now().date()
            datestring = date_today.strftime("%Y-%m-%d")
            if (date[1] == datestring):
                print attrs[5][1]

response = urllib2.urlopen("https://github.com/stevex86")
html = response.read()
parser = RectParser()
parser.feed(html)
