from django.urls import path

from .views import AddUserView, ListUserView, ChangePassword

urlpatterns = [
    path("add_user/", AddUserView.as_view(), name="add_user"),
    path('list_user/', ListUserView.as_view(), name='list_user'),
    path('<int:pk>/change_password/', ChangePassword.as_view(), name="change_password")
]
