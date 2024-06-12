from django.urls import path

from . import views

app_name = "paciente"

# ProductoCategoria
urlpatterns = [
    path("", views.home, name="home"),
    path("pacientecategoria/create/", views.PacienteCategoriaCreate.as_view(), name="Pacientecategoria_create"),
    path("pacientecategoria/list/", views.PacienteCategoriaList.as_view(), name="Pacientecategoria_list"),
    path("pacientecategoria/detail/<int:pk>", views.PacienteCategoriaDetail.as_view(), name="Pacientecategoria_detail"),
    path("pacientecategoria/update/<int:pk>", views.PacienteCategoriaUpdate.as_view(), name="Pacientecategoria_update"),
    path("pacientecategoria/delete/<int:pk>", views.PacienteCategoriaDelete.as_view(), name="Pacientecategoria_delete"),
    path("cervezas/", views.cervezas, name="cervezas"),
    path("gin/", views.gin, name="gin"),
    path("promociones/", views.promociones, name="promociones"),
    path("quesos/", views.quesos, name="quesos"),
    
    
]

# paciente
urlpatterns += [
    path("editar_paciente/", views.editar_paciente, name="editar_paciente"),
    path("paciente/list/", views.PacienteList.as_view(), name="paciente_list"),
    path("paciente/create/", views.PacienteCreate.as_view(), name="paciente_create"),
    path("paciente/detail/<int:pk>", views.PacienteDetail.as_view(), name="paciente_detail"),
    path("paciente/update/<int:pk>", views.PacienteUpdate.as_view(), name="paciente_update"),
    path("paciente/delete/<int:pk>", views.PacienteDelete.as_view(), name="paciente_delete"),
    
]
