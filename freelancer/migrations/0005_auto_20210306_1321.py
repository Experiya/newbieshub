# Generated by Django 3.1.5 on 2021-03-06 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelancer', '0004_auto_20210306_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freelancer',
            name='image',
            field=models.ImageField(default='', upload_to='freelancer/images'),
        ),
    ]
