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
            name='Hospitalisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_admission', models.DateField(auto_now_add=True)),
                ('date_sortie', models.DateField(blank=True, null=True)),
                ('motif_admission', models.TextField()),
                ('diagnostic_final', models.TextField(blank=True)),
                ('clinical', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinical.clinical')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
        ),
        migrations.CreateModel(
            name='SuiviQuotidien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_suivi', models.DateField(auto_now_add=True)),
                ('symptomes', models.TextField()),
                ('evolution', models.TextField()),
                ('traitement_administre', models.TextField(blank=True)),
                ('clinical', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinical.clinical')),
                ('hospitalisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitalisation.hospitalisation')),
            ],
        ),
    ]
