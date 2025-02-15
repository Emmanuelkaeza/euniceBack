# Generated by Django 5.0.6 on 2024-06-22 19:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clinical', '0001_initial'),
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_consultation', models.DateField(auto_now_add=True)),
                ('symptomes', models.TextField()),
                ('diagnostic', models.TextField()),
                ('recommandations', models.TextField(blank=True)),
                ('examens_demandes', models.TextField(blank=True)),
                ('is_hospitaliser', models.BooleanField(default=False)),
                ('clinical', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinical.clinical')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
        ),
    ]
