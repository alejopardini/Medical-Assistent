from django.contrib import admin

# Register your models here.
from . import models

admin.site.site_title = "pacientes"


class PacienteCategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    list_display_links = ("nombre",)


class PacienteAdmin(admin.ModelAdmin):
    list_display = (
        "categoria_id",
        "nombre",
        "unidad_medida",
        "cantidad",
        "precio",
        "fecha_actualizacion",
    )
    list_display_links = ("nombre",)
    search_fields = ("nombre",)
    ordering = ("categoria_id", "nombre")
    list_filter = ("categoria_id",)
    date_hierarchy = "fecha_actualizacion"


admin.site.register(models.PacienteCategoria,PacienteCategoriaAdmin)
admin.site.register(models.Paciente, PacienteAdmin)
