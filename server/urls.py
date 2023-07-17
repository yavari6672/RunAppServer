from django.urls import path

from . import views

# app_name = 'server'
urlpatterns = [
    path("", views.index, name="server_index"),
]
