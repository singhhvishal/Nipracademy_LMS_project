# Generated by Django 4.2.10 on 2024-03-23 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Nipracademy', '0020_staffs_delete_faculty'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staffs',
            old_name='faculty_image',
            new_name='image',
        ),
    ]
