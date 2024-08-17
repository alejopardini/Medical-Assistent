from django.db import models
from django.utils import timezone
from datetime import date
from paciente.models import Paciente

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='consultas')
    fecha = models.DateField(default=timezone.now)
    motivo = models.CharField(max_length=200)
    observaciones = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Consulta de {self.paciente} el {self.fecha}"

    class Meta:
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"