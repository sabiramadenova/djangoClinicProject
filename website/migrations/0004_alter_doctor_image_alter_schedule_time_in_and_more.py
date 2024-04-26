# Generated by Django 5.0.2 on 2024-04-17 08:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_doctor_image_alter_schedule_time_in_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='C:\\Projects\\ProfessionalProjects\\clinicProject\\media/'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='time_in',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 17, 14, 26, 14, 98269)),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='time_out',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 17, 14, 26, 14, 98269)),
        ),
    ]