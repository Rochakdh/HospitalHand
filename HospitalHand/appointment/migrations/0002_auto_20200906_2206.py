# Generated by Django 3.1 on 2020-09-06 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='authentication_token',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='appointment_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='appointment_time',
            field=models.TimeField(blank=True, default=None, null=True),
        ),
    ]