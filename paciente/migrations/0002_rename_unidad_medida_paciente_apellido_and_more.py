# Generated by Django 5.0.6 on 2024-08-08 21:29

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paciente',
            old_name='unidad_medida',
            new_name='apellido',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='fecha_actualizacion',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='precio',
        ),
        migrations.AddField(
            model_name='paciente',
            name='archivos',
            field=models.FileField(blank=True, null=True, upload_to='pacientes/archivos/'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='celular',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='discapacidad',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='paciente',
            name='discapacidad_detalle',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='fecha_inicio',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='historia_clinica',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='nacionalidad',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='ultima_consulta',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='categoria_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='paciente.pacientecategoria', verbose_name='categoría'),
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('motivo', models.CharField(max_length=200)),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultas', to='paciente.paciente')),
            ],
            options={
                'verbose_name': 'Consulta',
                'verbose_name_plural': 'Consultas',
            },
        ),
    ]
