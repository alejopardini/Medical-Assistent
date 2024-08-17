from django.db import models
from django.utils import timezone
from datetime import date
from paciente.models import Paciente

class ArchivoAdjunto(models.Model):
    paciente = models.ForeignKey(Paciente, related_name='adjuntos', on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='archivos/')
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre