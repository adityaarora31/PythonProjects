from django.urls import path
from . import views
from .views import NewUser, UserLogin, UpdateDetail

app_name = "login"

urlpatterns = [
    path('', views.index, name="login"),
    path('register/', NewUser.as_view(), name='register'),
    path('validate/', UserLogin.as_view(), name='validate_login'),
    path('update/<int:pk>/', UpdateDetail.as_view(), name='update'),
]
