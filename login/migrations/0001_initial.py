# Generated by Django 2.2 on 2019-04-03 04:52

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
            name='RegisterUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('phone_number', models.IntegerField()),
                ('description', models.CharField(blank=True, max_length=200)),
                ('is_seller', models.BooleanField(default=False)),
                ('photo', models.ImageField(default='static/images/default_user_photo.svg', upload_to='media/images/')),
                ('user', models.OneToOneField(max_length=40, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
