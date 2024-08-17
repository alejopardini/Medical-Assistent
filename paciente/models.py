from django.db import models
from django.utils import timezone
from datetime import date

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, null=True, blank=True)
    celular = models.CharField(max_length=20, null=True, blank=True)
    historia_clinica = models.TextField(null=True, blank=True)
    archivo = models.FileField(upload_to='pacientes/archivos/', null=True, blank=True)  # Asegúrate de que este campo esté aquí
    fecha_inicio = models.DateField(null=True, blank=True)
    ultima_consulta = models.DateField(null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    discapacidad = models.BooleanField(default=False)
    discapacidad_detalle = models.CharField(max_length=250, null=True, blank=True)

    def calcular_edad(self):
        if self.fecha_nacimiento is None:
            return None  # O alguna otra lógica que quieras usar en caso de que no haya fecha de nacimiento
        today = date.today()
        return today.year - self.fecha_nacimiento.year - (
            (today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day)
        )
    
    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"





