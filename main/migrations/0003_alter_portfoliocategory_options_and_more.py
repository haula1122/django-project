# Generated by Django 4.1.3 on 2022-12-04 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_service_bootstrap_icon_class'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='portfoliocategory',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='subscribe',
            options={'verbose_name_plural': 'Subscribers'},
        ),
    ]
