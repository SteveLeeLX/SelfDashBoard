from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.inbox, name='inbox'),
    url(r'^compose/', views.compose, name='compose'),
    url(r'^detail/', views.detail, name='detail'),
]
