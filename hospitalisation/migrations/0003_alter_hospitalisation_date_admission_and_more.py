# Generated by Django 5.0.6 on 2024-06-23 14:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalisation', '0002_examenposthospitalisation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospitalisation',
            name='date_admission',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='suiviquotidien',
            name='date_suivi',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
