# Generated by Django 3.1 on 2020-09-03 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0017_auto_20200903_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
