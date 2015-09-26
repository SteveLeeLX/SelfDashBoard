import datetime

from django.views.generic import ListView

from .models import Feed
from .syncfeed import create_new_feed
# Create your views here.

class DailyFeedView(ListView):
    create_new_feed(rss_links=['http://www.36kr.com/feed?1.0', 'http://zhihurss.miantiao.me/dailyrss', ])

    template_name = "dailyfeed/dailyfeed.html"

    time_now = datetime.datetime.now()

    context_object_name = "feed_list"

    queryset = Feed.objects.filter(date_published__day=int(datetime.datetime.today().day)).order_by('-date_published')  # add filter for time here
