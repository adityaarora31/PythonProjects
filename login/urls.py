from django.urls import path
from . import views
from .views import NewUser, UserLogin, UpdateDetail
from django.contrib.auth import views as auth_views
app_name = "login"

urlpatterns = [
    path('', views.index, name="login"),
    path('register/', NewUser.as_view(), name='register'),
    path('dashboard/', UserLogin.as_view(), name='dashboard'),
    path('update/<int:pk>/', UpdateDetail.as_view(), name='update'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login.html'), name="logout"),
    path('/homepage', views.homepage, name="homepage"),
]
