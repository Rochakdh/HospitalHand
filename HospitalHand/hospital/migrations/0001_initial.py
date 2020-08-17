# Generated by Django 3.1 on 2020-08-17 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0012_auto_20200816_0515'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_address', models.CharField(max_length=150)),
                ('contact_number', models.IntegerField()),
                ('name', models.CharField(max_length=150)),
                ('doctors', models.ManyToManyField(to='categories.Doctor')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
