from django.urls import path
from .views import leverkey, menu
from .views import category

urlpatterns = [
    path ("", menu),
    path ("category/", category),
    path ("category/leverkey/", leverkey),
]