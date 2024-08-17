from django.contrib import admin
from .models import Turno

class TurnoAdmin(admin.ModelAdmin):
    # Combina fecha y hora para mostrar como 'fecha_hora'
    list_display = ("paciente", "fecha", "hora", "descripcion", "estado")
    list_display_links = ("paciente", "fecha")
    search_fields = ("paciente__nombre", "descripcion")  # Suponiendo que 'paciente' tiene un campo 'nombre'
    ordering = ("fecha", "hora", "paciente")
    date_hierarchy = "fecha"  # Usar 'fecha' para la jerarquía de fechas

admin.site.register(Turno, TurnoAdmin)
