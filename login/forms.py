import re
from django import forms
from django.contrib.auth.models import User
from .models import RegisterUser
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    phone_number = forms.IntegerField()
    description = forms.CharField()
    is_seller = forms.CheckboxInput()

    def clean(self):

        form_data = self.cleaned_data
        number_regex = re.compile("^\d{10}$")
        username_regex = re.compile("^(?=.{8,20}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$")
        user_email = self.cleaned_data.get('user_email')

        try:
            match = User.objects.get(email=user_email)

        except User.DoesNotExist as err:
            self.add_error('user_email', "Email already exists ! ")

        if not re.match(number_regex, str(form_data.get("phone_number"))):
            self.add_error('phone_number', "The phone number must be in Indian Format")

        if not re.match(username_regex, str(form_data.get("username"))):
            self.add_error('username', "Username is not valid !")

        return form_data

    class Meta:
        model = RegisterUser
        fields = ['username', 'user_email', 'first_name',
                  'last_name', 'phone_number', 'password1',
                  'password2', 'description', 'is_seller',
                  'photo']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())


# class UpdateDetails(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name']
