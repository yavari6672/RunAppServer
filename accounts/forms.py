from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserModel
from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.CharField(required=False)

    def save(self, commit=True):
        if commit:
            user = User.objects.create_user(
                username=self.cleaned_data['username'],
                email=self.cleaned_data['email'],
                password=self.cleaned_data['password1'],
                first_name=self.cleaned_data['first_name'],
                last_name=self.cleaned_data['last_name']
            )
        return user


class UserChangePasswordForm(forms.Form):
    password = forms.CharField(max_length=150, widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=150, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password != password_confirm:
            raise ValidationError('password does not match')
        return self.cleaned_data


class EditUserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'email']


class CustomGroupCreationForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']


class DeleteUserForm(forms.Form):
    User = forms.BooleanField(label='Are you sure you want to delete User ?',
                              error_messages={'required': 'Please Checked Box For Delete User'})


class DeleteGroupForm(forms.Form):
    User = forms.BooleanField(label='Are you sure you want to delete Group ?',
                              error_messages={'required': 'Please Checked Box For Delete Group'})
