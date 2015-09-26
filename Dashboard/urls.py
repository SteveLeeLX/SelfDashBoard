"""Dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from emailbox import urls as email_urls
from oauth2_auth import urls as oauth2_urls

from . import views
from account_auth import views as auth_views
from dailyfeed import views as feed_views
from mycalendar import views as calendar_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', auth_views.login, name='login'),
    url(r'^inbox/', include(email_urls),name='inbox'),
    url(r'^logout/', auth_views.logout, name='logout'),
    url(r'^oauth2/', include(oauth2_urls, namespace="oauth2")),
    url(r'^feed/', feed_views.DailyFeedView.as_view(), name='dailyfeed'),
    url(r'^calendar/', calendar_views.calendar_view, name='calendar'),
    url(r'^$', views.index, name='index'),
]
