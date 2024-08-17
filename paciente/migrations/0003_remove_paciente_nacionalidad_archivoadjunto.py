# Generated by Django 5.0.6 on 2024-08-11 21:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0002_rename_unidad_medida_paciente_apellido_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='nacionalidad',
        ),
        migrations.CreateModel(
            name='ArchivoAdjunto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archivo', models.FileField(upload_to='archivos/')),
                ('nombre', models.CharField(max_length=255)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adjuntos', to='paciente.paciente')),
            ],
        ),
    ]
