# Generated by Django 3.1 on 2020-09-02 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0028_appointment_authentication_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='authentication_token',
            field=models.CharField(max_length=200),
        ),
    ]