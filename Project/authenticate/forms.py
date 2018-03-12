from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from authenticate import models


class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$')
    email = forms.EmailField(max_length=200, help_text='Required')
    profile_photo = forms.ImageField(max_length=None, allow_empty_file=True, required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'phone_number', 'email', 'password1',
                  'password2', 'profile_photo')
