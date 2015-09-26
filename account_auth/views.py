from django.shortcuts import render_to_response, RequestContext, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout

# Create your views here.
def login(request):
    '''
    Login View
    '''
    template_name = 'registration/login.html'
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(email=request.POST['username'], password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return redirect('/')
    else:
        form = AuthenticationForm()
    return render_to_response('registration/login.html', {
        'form': form,
    }, context_instance=RequestContext(request))


def logout(request):
    '''
    Log the user out
    '''
    auth_logout(request)
    return redirect('/login')
