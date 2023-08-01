from django.urls import path
from django.views.generic import TemplateView
from .views import AddUserView, ListUserView, change_password, \
    EditUserView, DeleteUserView, ListGroupView, GroupDetailView, UserPermissionsView
from .forms import CustomUserCreationForm

urlpatterns = [
    path("add_user/", AddUserView.as_view(), name="add_user"),
    path('list_user/', ListUserView.as_view(), name='list_user'),
    path('<int:pk>/change_password/', change_password, name="change_password"),
    path('<int:user_id>/edit_user/', EditUserView.as_view(), name="edit_user"),
    path('<int:pk>/delete_user/', DeleteUserView.as_view(), name="delete_user"),

    path('list_group/', ListGroupView.as_view(), name='list_group'),
    path('<int:pk>/group_detail/', GroupDetailView.as_view(), name='group_detail'),
    path('<int:pk>/user_permissions/', UserPermissionsView.as_view(), name='user_permissions'),
]
