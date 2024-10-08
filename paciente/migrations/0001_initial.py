# Generated by Django 5.0.6 on 2024-06-12 01:31

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PacienteCategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, unique=True)),
                ('descripcion', models.CharField(blank=True, max_length=250, null=True, verbose_name='descripción')),
            ],
            options={
                'verbose_name': 'categoría de Paciente',
                'verbose_name_plural': 'categorías de Pacientes',
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('unidad_medida', models.CharField(max_length=100)),
                ('cantidad', models.FloatField()),
                ('precio', models.FloatField()),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='descripción')),
                ('fecha_actualizacion', models.DateField(blank=True, default=django.utils.timezone.now, editable=False, null=True, verbose_name='fecha de actualización')),
                ('categoria_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='paciente.pacientecategoria', verbose_name='categoría de producto')),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
            },
        ),
    ]
