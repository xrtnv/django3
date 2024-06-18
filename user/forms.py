from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm

from user.models import User


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True, max_length=30)
    password1 = forms.CharField(required=True, max_length=30)
    password2 = forms.CharField(required=True, max_length=30)

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class ResetUserPasswordForm(PasswordResetForm):
    email = forms.EmailField(required=True, max_length=30)
