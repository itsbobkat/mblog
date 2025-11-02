from django.urls import path

from . import views

urlpatterns = [
    path("", views.homepage),
    path("favicon.ico", views.favicon),
]
