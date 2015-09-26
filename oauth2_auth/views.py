from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponseRedirect
from oauth2client.client import OAuth2WebServerFlow

def FlowView(request):
    flow = OAuth2WebServerFlow(client_id='766940716907-503o8rcfr78s50elpro8hcl8u3th0roe.apps.googleusercontent.com',
                           client_secret='2TCPOme3ZWNMmSic7rFye6i3',
                           scope='https://www.googleapis.com/auth/calendar',
                           redirect_uri='http://localhost:8000/oauth2/callback/')
    auth_uri = flow.step1_get_authorize_url()
    return HttpResponseRedirect(auth_uri)


def CallBackView(request):
    flow = OAuth2WebServerFlow(client_id='766940716907-503o8rcfr78s50elpro8hcl8u3th0roe.apps.googleusercontent.com',
                           client_secret='2TCPOme3ZWNMmSic7rFye6i3',
                           scope='https://www.googleapis.com/auth/calendar',
                           redirect_uri='http://localhost:8000/oauth2/callback/')
    code = request.GET('code')
    credentials = flow.step2_exchange(code)
