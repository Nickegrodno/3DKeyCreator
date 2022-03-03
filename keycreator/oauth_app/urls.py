from django.urls import path
from .views import mainmenu
from .views import category

urlpatterns = [
    path ("", mainmenu),
    path ("category/", category),
]