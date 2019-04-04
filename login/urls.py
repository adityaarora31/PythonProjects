from django.urls import path
from . import views
from .views import NewUser, UserLogin, show

urlpatterns = [
    path('', views.index, name="login"),
    path('register/', NewUser.as_view(), name='register'),
    path('validate/', UserLogin.as_view(), name='validate_login'),
    path('dashboard/', show, name='dashboard'),
]
