from django.urls import path
from .views import PropertyOperations, UpdateProperty, ViewProperty, ViewSpecificProperty, search_property, property_view, make_query

urlpatterns = [
    #path('', PropertyOperations.as_view, name='name'),
    path('register_property/', PropertyOperations.as_view(), name='register_property'),
    path('update_property/<int:pk>/', UpdateProperty.as_view(), name='update_property'),
    path('view_property/', ViewProperty.as_view(), name='view_property'),
    path('view_property/<int:pk>/', ViewSpecificProperty.as_view(), name='view_specific_property'),
    path('search/', search_property, name="search"),
    path('property_view/', property_view, name="seller_view_property"),
    path('query/<int:pid>', make_query, name="make_query")
]
