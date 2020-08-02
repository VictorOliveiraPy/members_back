# Generated by Django 3.0.8 on 2020-08-01 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('surname', models.CharField(max_length=80)),
                ('phone', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=120)),
                ('photo', models.ImageField(upload_to='members_profile')),
            ],
        ),
    ]
