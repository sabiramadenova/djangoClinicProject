# Generated by Django 5.0.2 on 2024-03-27 08:52

import datetime
import pathlib
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_post_text_alter_schedule_time_in_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=pathlib.PureWindowsPath('C:/Projects/ProfessionalProjects/clinicProject/media')),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='time_in',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 27, 14, 52, 39, 664289)),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='time_out',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 27, 14, 52, 39, 664289)),
        ),
    ]