from django.urls import path
from .views import menu
from .views import category

urlpatterns = [
    path ("", menu),
    path ("category/", category),
]