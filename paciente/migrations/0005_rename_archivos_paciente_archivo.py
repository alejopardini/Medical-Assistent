# Generated by Django 5.0.6 on 2024-08-14 03:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0004_remove_consulta_paciente_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paciente',
            old_name='archivos',
            new_name='archivo',
        ),
    ]
