# Generated by Django 3.1.7 on 2021-03-31 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0012_auto_20210331_1743'),
        ('freelancer', '0018_auto_20210331_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='trashFiles',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.FileField(default='', upload_to='freelancer/files')),
                ('flag', models.CharField(max_length=50)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
                ('freelancer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freelancer.freelancer')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.project')),
            ],
        ),
        migrations.AlterField(
            model_name='timelinefc',
            name='flag',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='files',
        ),
    ]
