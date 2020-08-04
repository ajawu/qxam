from django.shortcuts import render
from django.http import HttpResponseRedirect


def home_page_view(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            pass  # render staff dashboard page
        else:
            pass  # render student dashboard page
    else:
        return HttpResponseRedirect('/accounts/login/')


def dummy_page(request):
    return render(request, 'accounts/signup.html', {})
