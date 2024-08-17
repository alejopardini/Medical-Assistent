from django.db import models
from datetime import timedelta
from django.conf import settings
from django.core.exceptions import ValidationError


class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    historial = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Profesional(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} ({self.especialidad})"

class Turno(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateField()  # Nuevo campo para la fecha
    hora = models.TimeField()  # Nuevo campo para la hora
    duracion = models.DurationField(default=timedelta(hours=1))
    descripcion = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=[('pendiente', 'Pendiente'), ('confirmado', 'Confirmado'), ('cancelado', 'Cancelado')])
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.paciente} - {self.fecha} {self.hora}'

    def clean(self):
        start_time = self.hora
        end_time = (datetime.combine(date.today(), start_time) + self.duracion).time()

        overlapping_turnos = Turno.objects.filter(
            fecha=self.fecha,
            hora__lt=end_time,
            hora__gte=start_time
        ).exclude(pk=self.pk)

        if overlapping_turnos.exists():
            raise ValidationError('Ya existe un turno en el mismo horario.')

        if not (self.hora >= time(8, 0) and self.hora < time(18, 0)):
            raise ValidationError('El turno debe estar entre las 8:00 y las 18:00.')

        if self.hora >= time(12, 0) and self.hora < time(14, 0):
            raise ValidationError('No se permiten turnos entre las 12:00 y las 14:00.')
