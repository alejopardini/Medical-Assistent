from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("usuario/", include("usuario.urls")),
    path("paciente/", include("paciente.urls")),
    path('turnos/', include('turnos.urls')),
]