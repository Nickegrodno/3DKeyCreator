#from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Начало разработки сайта 3D Key Creator.")
