# Generated by Django 3.1.7 on 2021-03-20 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_request'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Request',
            new_name='requestByClient',
        ),
    ]
