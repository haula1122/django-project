# Generated by Django 4.1.3 on 2022-12-04 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acct', '0002_alter_socialmedia_options_profile_team_member'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
    ]
