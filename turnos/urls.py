from django.urls import path
from . import views

app_name = 'turnos'


urlpatterns = [
    path('turnos/', views.turnos, name='turnos'),
    path('turnos/lista/', views.listar_turnos, name='listar_turnos'), 
    path('turnos/nuevo/', views.crear_turno, name='crear_turno'),
    path('<int:id>/', views.detalle_turno, name='detalle_turno'),
    path('<int:id>/editar/', views.editar_turno, name='editar_turno'),
    path('<int:id>/eliminar/', views.eliminar_turno, name='eliminar_turno'),
]

