# Generated by Django 4.2.10 on 2024-03-01 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nipracademy', '0003_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
