# Generated by Django 2.2 on 2019-04-12 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property_operations', '0003_enquiry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enquiry',
            old_name='enquiry_person_email',
            new_name='enquiry_person',
        ),
    ]