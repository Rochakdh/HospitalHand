# Generated by Django 3.1 on 2020-08-21 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0003_auto_20200821_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='contact_number',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]