from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^flow/', views.FlowView, name='flow'),
    url(r'^callback/', views.CallBackView, name='oauth2_return'),
)