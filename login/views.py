from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import FormView, UpdateView
from .forms import UserRegisterForm, LoginForm
from .models import RegisterUser


def index(request):
    return render(request, 'login.html')


def homepage(request):
    return render(request, 'homepage.html')


class NewUser(FormView):
    form_class = UserRegisterForm
    template_name = 'register.html'

    def form_valid(self, form):
        form.save()
        return render(request=self.request, template_name='login.html')

    def form_invalid(self, form):
        return render(request=self.request, template_name='register.html', context={'form': form.errors})


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
            first_name = RegisterUser.objects.get(username=username).first_name
            last_name = RegisterUser.objects.get(username=username).last_name
            user_email = RegisterUser.objects.get(username=username).user_email
            user_description = RegisterUser.objects.get(username=username).description
            is_seller = RegisterUser.objects.get(username=username).is_seller
            user_id = RegisterUser.objects.get(username=username).user_id
            logged_in = True
            return show_dashboard(request=self.request, username=username, first_name=first_name,
                                  last_name=last_name, user_email=user_email, user_description=user_description,
                                  is_seller=is_seller, user_id=user_id, logged_in=logged_in)
        else:
            return render(request=self.request, template_name='login.html', context={'error': 'Sorry ! Unable to login !'})


@login_required
def show_dashboard(request, username, first_name, last_name, user_email, user_description, is_seller, user_id, logged_in):
    if request.session['login_switch']:
        return render(request, 'dashboard.html', context={'username': username, 'first_name': first_name,
                                                          'last_name': last_name, 'user_email': user_email,
                                                          'user_description': user_description, 'is_seller': is_seller,
                                                          'user_id': user_id, 'logged_in': logged_in})
    else:
        return render(request, 'login.html')


class UpdateDetail(LoginRequiredMixin, UpdateView):
    model = RegisterUser
    fields = ['first_name', 'last_name', 'user_email', 'description']
    template_name = 'update.html'
