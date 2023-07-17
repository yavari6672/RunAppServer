from django.urls import path

from . import views

urlpatterns = [
    path("main/", views.main_index, name="main_index"),
    path('', views.index, name='index')
]
