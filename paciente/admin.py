from django.contrib import admin
from .models import Paciente
from consultas.models import Consulta

admin.site.site_title = "Gestión de Pacientes"

class ConsultaInline(admin.TabularInline):
    model = Consulta
    extra = 0

class PacienteAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "apellido",
        "email",
        "fecha_nacimiento",
    )
    inlines = [ConsultaInline]
    list_display_links = ("nombre", "apellido")
    search_fields = ("nombre", "apellido")
    ordering = ("nombre", "apellido")
    date_hierarchy = "fecha_nacimiento"  # Asegúrate de que 'fecha_nacimiento' sea un campo en el modelo

admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Consulta)
