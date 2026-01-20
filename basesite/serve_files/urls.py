from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("fetch/", views.file_fetch, name="file_fetch"),
    path("display/", views.file_display, name="file_display"),
]