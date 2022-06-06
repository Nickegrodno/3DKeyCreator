from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
# from allauth.account.decorators import verified_email_required
from django.template import RequestContext

# Create your views here.

# @verified_email_required
@login_required(login_url="")
def menu(request) :
    return render(request, "menu.html")

@login_required(login_url="")
def category(request) :
    return render(request, "category.html")

@login_required(login_url="")
def leverkey(request) :
    return render(request, "leverkey.html")

# HTTP Error 400
def handler404(request, exception, template_name="404.html"):
    response = render(template_name)
    response.status_code = 404
    return response