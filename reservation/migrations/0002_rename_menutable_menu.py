# Generated by Django 4.2.5 on 2023-10-07 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MenuTable',
            new_name='Menu',
        ),
    ]