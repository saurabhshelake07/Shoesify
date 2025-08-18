from django.urls import path
from .views import first_view, addShoeView,updateShoeView, deleteShoeView, showShoeView


urlpatterns=[
    path("first/",first_view),
    path("add/",addShoeView, name="add-shoes"),
    path("update/<i>/",updateShoeView, name="update-shoes"),
    path("delete/<i>/",deleteShoeView, name="delete-shoes"),
    path("show/",showShoeView, name="show-shoes"),

]