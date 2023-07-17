from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


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


class UserChangePasswordForm(forms.ModelForm):
    class Meta:
        fields = ['']

    def save(self, pk, commit=True):
        if commit:
            user = User.objects.get(pk=pk)
            user.password = self.cleaned_data['password1']
            user.save()
        return user
