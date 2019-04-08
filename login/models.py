from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class RegisterUser(User):

    user = models.OneToOneField(User, max_length=40, on_delete=models.CASCADE, parent_link=True)
    user_email = models.EmailField(max_length=50, unique=True)
    phone_number = models.IntegerField()
    description = models.CharField(max_length=200, blank=True)
    is_seller = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='media/images/', default='static/images/default_user_photo.svg')

    def __str__(self):
        return self.user_email

    def get_absolute_url(self):
        return reverse('login')



#
# class Property(models.Model):
#     property_title = models.CharField(max_length=20, required=True)
#     property_address = models.CharField(max_length=20, blank=False)
#     property_city = (
#         ('Panaji', 'Panaji'),
#         ('New Delhi', 'New Delhi'),
#         ('Gurugram', 'Gurugram'),
#         ('Chandigarh', 'Chandigarh'),
#     )
#     property_state = (
#         ('Goa', 'Goa'),
#         ('Delhi', 'Delhi'),
#         ('Haryana', 'Haryana'),
#         ('Punjab', 'Punjab'),
#     )
#     property_pin = models.IntegerField(blank=False)
#     property_price = models.IntegerField(blank=False)
#     property_bedroom = models.IntegerField(default=1)
#     property_bathroom = models.IntegerField(default=1)
#     property_sq_feet = models.IntegerField(blank=False)
#     property_lot_size = models.IntegerField(blank=False)
#     property_garage = models.IntegerField(default=0)
#     property_listing_date = models.DateField(auto_now_add=True)
#     property_description = models.CharField(max_length=200)
#     property_seller_name = models.ForeignKey()
#
#
# class PropertyImage(models.Model):
#     property_id = models.ForeignKey(Property, on_delete=models.CASCADE)
#     property_image = models.ImageField(upload_to='/images')
