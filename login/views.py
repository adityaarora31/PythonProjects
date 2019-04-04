from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import FormView
from .forms import UserRegisterForm, LoginForm
from .models import RegisterUser


def index(request):
    return render(request, 'login.html')


class NewUser(FormView):
    form_class = UserRegisterForm
    template_name = 'register.html'

    def post(self, request, *args, **kwargs):
        forms = UserRegisterForm(request.POST)
        if forms.is_valid():
            forms.save()
            return HttpResponse(request, 'login.html')
        else:
            return HttpResponse(request, 'register.html')


class UserLogin(FormView):
    form_class = LoginForm
    template_name = 'login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        present_user = authenticate(self.request, username=username, password=password)
        if present_user is not None:
            login(self.request, present_user)
            self.request.session['present_user'] = username
            self.request.session['login_switch'] = True
            self.request.session['is_seller'] = RegisterUser.objects.get(username=username).is_seller
            return HttpResponse(self.request, 'dashboard.html')
        else:
            return HttpResponse(self.request, 'login.html', {'error': 'Sorry ! Unable to login'})
