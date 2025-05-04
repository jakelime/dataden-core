# api/urls.py
from django.urls import path
from . import views  # Import views from the current directory

app_name = "gmailreader"

urlpatterns = [
    path("hello/", views.hello_world_view, name="hello_world"),
]
