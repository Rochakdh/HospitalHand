# Generated by Django 3.1 on 2020-08-15 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='department',
            field=models.CharField(choices=[('Anesthesiology', 'Anesthesiology'), ('Cardiology and Cardiac Surgery', 'Cardiology and Cardiac Surgery'), ('Cardiothoracic and Vascular Surgery', 'Cardiothoracic and Vascular Surgery')], max_length=100),
        ),
    ]