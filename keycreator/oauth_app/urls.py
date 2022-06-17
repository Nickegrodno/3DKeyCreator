from django.urls import path
from .views import leverkey, menu, leverkeycreate, sett, pinkey
from .views import category

urlpatterns = [
    path ("", menu),
    path ("category/", category),
    path ("sett/", sett),
    path ("category/leverkey/", leverkey),
    path ("category/pinkey/", pinkey),
    path ("category/leverkey/create", leverkeycreate),
    
]