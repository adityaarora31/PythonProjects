from django.urls import path
from .views import PropertyOperations

urlpatterns = [
    #path('', PropertyOperations.as_view, name='name'),
    path('register_property/', PropertyOperations.as_view(), name='reg_property'),
]
