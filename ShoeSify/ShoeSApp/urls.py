from django.urls import path
from .views import first_view


urlpatterns=[
    path("first/",first_view),
]