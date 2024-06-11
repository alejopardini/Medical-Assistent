from django.urls import path

from . import views

app_name = "cliente"

# ProductoCategoria
urlpatterns = [
    path("", views.home, name="home"),
    path("clientecategoria/create/", views.ClienteCategoriaCreate.as_view(), name="Clientecategoria_create"),
    path("clientecategoria/list/", views.ClienteCategoriaList.as_view(), name="Clientecategoria_list"),
    path("clientecategoria/detail/<int:pk>", views.ClienteCategoriaDetail.as_view(), name="Clientecategoria_detail"),
    path("clientecategoria/update/<int:pk>", views.ClienteCategoriaUpdate.as_view(), name="Clientecategoria_update"),
    path("clientecategoria/delete/<int:pk>", views.ClienteCategoriaDelete.as_view(), name="Clientecategoria_delete"),
    path("cervezas/", views.cervezas, name="cervezas"),
    path("gin/", views.gin, name="gin"),
    path("promociones/", views.promociones, name="promociones"),
    path("quesos/", views.quesos, name="quesos"),
    
    
]

# cliente
urlpatterns += [
    path("editar_cliente/", views.editar_cliente, name="editar_cliente"),
    path("cliente/list/", views.ClienteList.as_view(), name="cliente_list"),
    path("cliente/create/", views.ClienteCreate.as_view(), name="cliente_create"),
    path("cliente/detail/<int:pk>", views.ClienteDetail.as_view(), name="cliente_detail"),
    path("cliente/update/<int:pk>", views.ClienteUpdate.as_view(), name="cliente_update"),
    path("cliente/delete/<int:pk>", views.ClienteDelete.as_view(), name="cliente_delete"),
    
]
