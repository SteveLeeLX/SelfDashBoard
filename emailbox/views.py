from django.shortcuts import render_to_response, RequestContext
from django.core.mail import send_mail

# Create your views here.
def inbox(request):
    return render_to_response('emailbox/mailbox.html', locals(), RequestContext(request))


def compose(request):
    template_name = 'emailbox/mail_compose.html'

    if request.method == 'POST':
        send_mail('Subject here', 'Here is the message.', 'from@example.com',
                  ['to@example.com'], fail_silently=False)
    return render_to_response('emailbox/mail_compose.html', locals(), RequestContext(request))


def detail(request):
    return render_to_response('emailbox/mail_detail.html', locals(), RequestContext(request))
