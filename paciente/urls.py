from django.urls import path
from . import views

app_name = "paciente"

urlpatterns = [
    path("", views.home, name="home"),
    path("editar_paciente/", views.editar_paciente, name="editar_paciente"),
    path("paciente/list/", views.PacienteListView.as_view(), name="paciente_list"),
    path("paciente/create/", views.PacienteCreateView.as_view(), name="paciente_create"),
    path("paciente/detail/<int:pk>", views.PacienteDetailView.as_view(), name="paciente_detail"),
    path("paciente/update/<int:pk>", views.PacienteUpdateView.as_view(), name="paciente_update"),
    path("paciente/delete/<int:pk>", views.PacienteDeleteView.as_view(), name="paciente_delete"),
]
