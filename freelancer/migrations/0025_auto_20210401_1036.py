# Generated by Django 3.1.7 on 2021-04-01 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelancer', '0024_auto_20210401_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='client',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='report',
            name='flag',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='report',
            name='freelancer',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterUniqueTogether(
            name='report',
            unique_together={('freelancer', 'client')},
        ),
    ]
