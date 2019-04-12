from django.contrib.auth.models import User
from django.db import models
from login.models import RegisterUser


class Property(models.Model):
    property_seller_name = models.ForeignKey(User, on_delete=models.CASCADE)
    property_title = models.CharField(max_length=20, blank=False)
    property_address = models.CharField(max_length=20, blank=False)
    PROPERTY_CITY_CHOICES = (
        ('Panaji', 'Panaji'),
        ('New Delhi', 'New Delhi'),
        ('Gurugram', 'Gurugram'),
        ('Chandigarh', 'Chandigarh'),
    )
    property_city = models.CharField(max_length=10, choices=PROPERTY_CITY_CHOICES)
    PROPERTY_STATE_CHOICES = (
        ('Goa', 'Goa'),
        ('Delhi', 'Delhi'),
        ('Haryana', 'Haryana'),
        ('Punjab', 'Punjab'),
    )
    property_state = models.CharField(max_length=10, choices=PROPERTY_STATE_CHOICES)
    property_pin = models.IntegerField(blank=False)
    property_price = models.IntegerField(blank=False)
    property_bedroom = models.IntegerField(default=1)
    property_bathroom = models.IntegerField(default=1)
    property_sq_feet = models.IntegerField(blank=False)
    property_lot_size = models.IntegerField(blank=False)
    property_garage = models.IntegerField(default=0)
    property_listing_date = models.DateField(auto_now_add=True)
    property_description = models.CharField(max_length=200)
    property_image = models.ImageField(upload_to='media/property', blank=False)
    property_image2 = models.ImageField(upload_to='media/property', default="", blank=True)
    property_image3 = models.ImageField(upload_to='media/property', default="", blank=True)
    property_image4 = models.ImageField(upload_to='media/property', default="", blank=True)


class Enquiry(models.Model):
    enquiry_property = models.ForeignKey(Property, on_delete=models.CASCADE)
    enquiry_description = models.TextField(max_length=200, blank=False)
    enquiry_date = models.DateField(auto_now_add=True)
    enquiry_person = models.ForeignKey(RegisterUser, on_delete=models.CASCADE, default='')

