# Generated by Django 3.1.7 on 2021-03-27 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('freelancer', '0011_auto_20210327_1326'),
        ('client', '0008_auto_20210327_1514'),
        ('chat', '0005_auto_20210327_1534'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='chatlits',
            unique_together={('freelancer', 'projectId', 'client')},
        ),
    ]
