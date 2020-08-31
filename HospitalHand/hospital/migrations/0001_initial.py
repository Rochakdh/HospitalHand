from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [

        ('categories', '0013_auto_20200818_1016'),

    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_address', models.CharField(max_length=150)),
                ('contact_number', models.IntegerField()),

                ('name', models.CharField(max_length=200)),

                ('doctors', models.ManyToManyField(to='categories.Doctor')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
