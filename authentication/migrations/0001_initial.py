# Generated by Django 4.1.1 on 2022-09-26 11:37

import authentication.hashers
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, validators=[authentication.hashers.ParameterCheckers.validate_name], verbose_name='Name')),
                ('email', models.EmailField(max_length=40, unique=True, validators=[authentication.hashers.ParameterCheckers.validate_email], verbose_name='Email')),
                ('username', models.CharField(max_length=25, unique=True, validators=[authentication.hashers.ParameterCheckers.validate_username], verbose_name='Username')),
                ('password1', models.CharField(max_length=100, validators=[authentication.hashers.ParameterCheckers.validate_password], verbose_name='Password')),
                ('password2', models.CharField(max_length=100, validators=[authentication.hashers.ParameterCheckers.validate_password], verbose_name='Re-Password')),
                ('phone', models.CharField(max_length=15, unique=True, validators=[authentication.hashers.ParameterCheckers.validate_phone], verbose_name='Phone')),
                ('address', models.CharField(max_length=120, verbose_name='Address')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'ordering': ['-date_created'],
            },
        ),
    ]
