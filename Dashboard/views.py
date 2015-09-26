from django.shortcuts import render_to_response, RequestContext
from django.contrib.auth.decorators import login_required

@login_required(login_url='login/')
def index(request):
    return render_to_response('index.html', locals(), RequestContext(request))
