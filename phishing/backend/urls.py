"""URLS specific to the event app."""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^check/$', views.check_website),
    url(r'^', views.dash),
]