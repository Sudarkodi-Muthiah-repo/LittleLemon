# Generated by Django 4.2.5 on 2023-11-21 01:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='No_of_guests',
            new_name='Noofguests',
        ),
    ]