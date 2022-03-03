from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="")
def mainmenu(request) :
    return render(request, "menu.html")

@login_required(login_url="")
def category(request) :
    return render(request, "category.html")