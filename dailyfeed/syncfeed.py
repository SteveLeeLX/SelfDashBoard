import feedparser
import datetime
from time import mktime

from .models import Feed

def create_new_feed(rss_links=[]):
    for rss_link in rss_links:
        feeds = feedparser.parse(rss_link)

        for entry in feeds.entries:
            f = Feed()
            try:
                f.title = entry.title
            except:
                pass

            try:
                f.author = entry.author
            except:
                pass

            try:
                f.date_published = datetime.datetime.fromtimestamp(int(mktime(entry.published_parsed))).strftime(
                    '%Y-%m-%d %H:%M:%S')
            except:
                pass

            try:
                f.link = entry.link
            except:
                pass

            try:
                f.content = entry.description.replace('<img ', '<img  class=\"img-responsive\" ')
            except:
                pass

            try:
                f.tags.add(entry.tags)
            except:
                pass

            try:
                f.save()
            except:
                pass
