from django.shortcuts import redirect
from .forms import CustomUserCreationForm, UserChangePasswordForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserModel
from main.views import CustomListView, CustomCreateView, CustomUpdateView
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render


class AddUserView(CustomCreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("list_user")
    success_message = 'Add User Successfully'
    template_name = "add_user.html"


class ListUserView(CustomListView):
    model = UserModel
    template_name = 'list_user.html'


class ChangePassword(CustomUpdateView):
    model = UserModel
    template_name = 'change_password.html'
    fields = ['username', 'password']
    success_url = reverse_lazy("list_user")
    success_message = 'Change Password Successfully'

    def get(self, request, pk, *args, **kwargs):
        user = UserModel.objects.get(pk=pk)
        form = UserChangePasswordForm(instance=user)
        return render(request, 'change_password.html',
                      {'form': form, 'first_name': user.first_name, 'last_name': user.last_name,
                       'username': user.username})
