# Generated by Django 3.1 on 2020-08-15 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0006_auto_20200815_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.department'),
        ),
    ]