"""
URL configuration for main app.
"""
from django.urls import path
from .views import HelloWorld

urlpatterns = [

    path("test/", HelloWorld.as_view(), name="hello world")
]