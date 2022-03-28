from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
#from allauth.account.decorators import verified_email_required

# Create your views here.

#@verified_email_required
@login_required(login_url="")
def menu(request) :
    return render(request, "menu.html")

@login_required(login_url="")
def category(request) :
    return render(request, "category.html")