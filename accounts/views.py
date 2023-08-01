from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from .forms import CustomUserCreationForm, UserChangePasswordForm, EditUserForm, DeleteUserForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserModel
from main.views import CustomListView, \
    CustomCreateView, CustomUpdateView, CustomFormView, CustomDeleteView, CustomDetailView
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.shortcuts import render
from main.env import BTN


class AddUserView(CustomCreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("list_user")
    success_message = 'Add User Successfully'
    template_name = "add_user.html"
    permission_required = 'user.can_add_user'


class ListUserView(CustomListView):
    model = UserModel
    template_name = 'list_user.html'
    permission_required = 'user.can_view_user'


class ListGroupView(CustomListView):
    model = Group
    template_name = 'list_group.html'
    permission_required = 'group.can_view_group'


@login_required
@permission_required('user.can_change_user')
def change_password(request, pk):
    user = get_object_or_404(User, pk=pk)
    context = {'first_name': user.first_name,
               'last_name': user.last_name,
               'username': user.username, 'BTN': BTN()}
    if request.method == 'POST':
        form = UserChangePasswordForm(request.POST)
        if form.is_valid():
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Changed Password is Successfully")
            return redirect('list_user')
    else:
        # user = User.objects.get(pk=pk)
        form = UserChangePasswordForm()

    context['form'] = form
    return render(request, 'change_password.html', context)


class EditUserView(CustomFormView):
    template_name = 'edit_user.html'
    form_class = EditUserForm
    success_url = reverse_lazy("list_user")
    success_message = 'Edit User Successfully'
    permission_required = 'user.can_change_user'

    def get(self, request, user_id, *args, **kwargs):
        self.kwargs['user_id'] = user_id
        user = User.objects.get(pk=user_id)
        form = EditUserForm(instance=user)
        return render(request, 'edit_user.html', {'form': form, 'BTN': BTN()})

    def post(self, request, user_id, *args, **kwargs):
        if self.kwargs['user_id'] and self.kwargs['user_id'] == user_id:
            return super().post(self, request, *args, **kwargs)
        else:
            self.success_message = 'Edit User Failed'
            redirect('list_user')

    def form_valid(self, form: EditUserForm):
        clean_data = form.cleaned_data
        if self.kwargs['user_id']:
            user = User.objects.get(pk=self.kwargs['user_id'])
            user.first_name = clean_data['first_name']
            user.last_name = clean_data['last_name']
            user.email = clean_data['email']
            user.save()
            return super().form_valid(form)
        else:
            self.success_message = 'Edit User Failed'
            redirect('list_user')


class DeleteUserView(CustomDeleteView):
    model = UserModel
    form_class = DeleteUserForm
    template_name = 'delete_user.html'
    success_url = reverse_lazy("list_user")
    success_message = 'Delete User Successfully'
    permission_required = 'user.can_delete_user'

    def get_context_data(self, **kwargs):
        user = get_object_or_404(User, pk=self.kwargs.get('pk'))
        context = super().get_context_data(**kwargs)
        context['first_name'] = user.first_name
        context['last_name'] = user.last_name
        context['username'] = user.username
        return context


class GroupDetailView(CustomDetailView):
    # model = User
    # queryset = User.objects.all()
    template_name = 'group_detail.html'
    permission_required = 'group.can_view_group'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['full_name'] = User.objects.get(pk=self.kwargs['pk']).get_full_name()
        return context

    def get_queryset(self):
        user = User.objects.get(pk=self.kwargs['pk'])
        queryset = user.groups.all().values()
        # print(queryset)
        return queryset


class UserPermissionsView(CustomDetailView):
    model = User
    template_name = 'user_permissions.html'
    permission_required = 'permission.can_view_permission'
