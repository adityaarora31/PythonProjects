# Generated by Django 2.2 on 2019-04-08 04:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_title', models.CharField(max_length=20)),
                ('property_address', models.CharField(max_length=20)),
                ('property_city', models.CharField(choices=[('Panaji', 'Panaji'), ('New Delhi', 'New Delhi'), ('Gurugram', 'Gurugram'), ('Chandigarh', 'Chandigarh')], max_length=10)),
                ('property_state', models.CharField(choices=[('Goa', 'Goa'), ('Delhi', 'Delhi'), ('Haryana', 'Haryana'), ('Punjab', 'Punjab')], max_length=10)),
                ('property_pin', models.IntegerField()),
                ('property_price', models.IntegerField()),
                ('property_bedroom', models.IntegerField(default=1)),
                ('property_bathroom', models.IntegerField(default=1)),
                ('property_sq_feet', models.IntegerField()),
                ('property_lot_size', models.IntegerField()),
                ('property_garage', models.IntegerField(default=0)),
                ('property_listing_date', models.DateField(auto_now_add=True)),
                ('property_description', models.CharField(max_length=200)),
                ('property_image', models.ImageField(upload_to='media/property')),
                ('property_image2', models.ImageField(blank=True, default='', upload_to='media/property')),
                ('property_image3', models.ImageField(blank=True, default='', upload_to='media/property')),
                ('property_image4', models.ImageField(blank=True, default='', upload_to='media/property')),
                ('property_seller_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
