# Generated by Django 3.1 on 2020-09-12 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0005_remove_appointment_authentication_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='authentication_token',
            field=models.CharField(default='12', max_length=200),
        ),
    ]
