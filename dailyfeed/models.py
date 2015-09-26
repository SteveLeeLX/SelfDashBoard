import feedparser
import datetime
from time import mktime

from django.db import models
from django.contrib import admin

from taggit.managers import TaggableManager

# Create your models here.
class FeedManager(models.Manager):
    @staticmethod
    def create_new_feed( rss_links=[]):
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

                return f


class Feed(models.Model):
    date_published = models.DateTimeField()
    title = models.CharField(max_length=200, unique=True)
    content = models.CharField(max_length=20000)
    author = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    tags = TaggableManager()
    unread = models.BooleanField(default=True)

    objects = FeedManager()

    def __unicode__(self):
        return self.title


admin.site.register(Feed)
