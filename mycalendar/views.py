from django.shortcuts import render_to_response, RequestContext

# Create your views here.
def calendar_view(request):
    return render_to_response('calendar/calendar.html', locals(), RequestContext(request))