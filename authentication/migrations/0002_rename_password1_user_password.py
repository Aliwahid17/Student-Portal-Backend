# Generated by Django 4.1.1 on 2022-09-26 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='password1',
            new_name='password',
        ),
    ]
