from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .models import Paciente
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from . import forms, models

def cervezas(request):
    cervezas_list = Paciente.objects.filter(categoria_id__nombre='Pacientes')
    context = {
        'cervezas_list': cervezas_list
    }
    return render(request, "paciente/cervezas.html",context)


def quesos(request):
    quesos_list = Paciente.objects.filter(categoria_id__nombre='Quesos')
    context = {
        'quesos_list': quesos_list
    }
    return render(request, "paciente/quesos.html",context)

def promociones(request):
    promociones_list = Paciente.objects.filter(categoria_id__nombre='Promociones')
    context = {
        'promociones_list': promociones_list
    }
    return render(request, 'paciente/promociones.html', context)


def home(request):
    return render(request, "paciente/index.html")

def editar_paciente(request):
    return render(request, "paciente/editar_producto.html")





def gin(request):
    productos_gin = Paciente.objects.filter(categoria_id__nombre='Gin Artesanal')
    context = {
        'productos_gin': productos_gin
    }
    return render(request, 'producto/gin.html', context)



class PacienteCategoriaList(ListView):
    model = models.PacienteCategoria


    def get_queryset(self) -> QuerySet:
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.PacienteCategoria.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.PacienteCategoria.objects.all()
        return object_list


class PacienteCategoriaCreate(CreateView):
    model = models.PacienteCategoria
    form_class = forms.PacienteCategoriaForm
    success_url = reverse_lazy("paciente:home")



class PacienteCategoriaUpdate(UpdateView):
    model = models.PacienteCategoria
    form_class = forms.PacienteCategoriaForm
    success_url = reverse_lazy("paciente:pacientecategoria_list")




class PacienteCategoriaDetail(DetailView):
    model = models.PacienteCategoria
    




class PacienteCategoriaDelete(LoginRequiredMixin, DeleteView):
    model = models.PacienteCategoria
    
    success_url = reverse_lazy("paciente:pacientecategoria_list")


# ***Paciente


class PacienteList(ListView):
    model = models.Paciente

    def get_queryset(self) -> QuerySet:
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.Paciente.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.Paciente.objects.all()
        return object_list


class PacienteCreate(CreateView):
    model = models.Paciente
    form_class = forms.PacienteForm
    success_url = reverse_lazy("paciente:home")


class PacienteUpdate(UpdateView):
    model = models.Paciente
    form_class = forms.PacienteForm
    success_url = reverse_lazy("paciente:paciente_list")


class PacienteDetail(DetailView):
    model = models.Paciente


class PacienteDelete(LoginRequiredMixin, DeleteView):
    model = models.Paciente
    success_url = reverse_lazy("´paciente:paciente_list")


