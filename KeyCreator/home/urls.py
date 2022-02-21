#home/urls.py

from django.urls import path
from . import views
from .views import SignUpView

urlpatterns = [

 path('', views.index, name = "home"),
 path('signup/', SignUpView.as_view(), name='signup'),
 
]