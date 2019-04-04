from django import forms
from .models import RegisterUser
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    phone_number = forms.IntegerField()
    description = forms.CharField()
    is_seller = forms.CheckboxInput()

    class Meta:
        model = RegisterUser
        fields = ['username', 'user_email', 'first_name',
                  'last_name', 'phone_number', 'password1',
                  'password2', 'description', 'is_seller',
                  'photo']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())
