from django.db import models
from django.utils import timezone


class ClienteCategoria(models.Model):
    """Categorías de Clientes"""

    nombre = models.CharField(max_length=200, unique=True)
    descripcion = models.CharField(max_length=250, null=True, blank=True, verbose_name="descripción")

    def __str__(self) -> str:
        """Representa una instancia del modelo como una cadena de texto"""
        return self.nombre

    class Meta:
        verbose_name = "categoría de Clientes"
        verbose_name_plural = "categorías de Clientes"


class Cliente(models.Model):
    categoria_id = models.ForeignKey(
        ClienteCategoria, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="categoría de producto"
    )
    nombre = models.CharField(max_length=100)
    unidad_medida = models.CharField(max_length=100)
    cantidad = models.FloatField()
    precio = models.FloatField()
    descripcion = models.TextField(null=True, blank=True, verbose_name="descripción")
    fecha_actualizacion = models.DateField(
        null=True, blank=True, default=timezone.now, editable=False, verbose_name="fecha de actualización"
    )

    def __str__(self) -> str:
        return f"{self.nombre} ({self.unidad_medida}) ${self.precio:.2f}"

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
