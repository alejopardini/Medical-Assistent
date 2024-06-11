from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .models import Cliente
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
    cervezas_list = Cliente.objects.filter(categoria_id__nombre='Clientes')
    context = {
        'cervezas_list': cervezas_list
    }
    return render(request, "cliente/cervezas.html",context)


def quesos(request):
    quesos_list = Cliente.objects.filter(categoria_id__nombre='Quesos')
    context = {
        'quesos_list': quesos_list
    }
    return render(request, "cliente/quesos.html",context)

def promociones(request):
    promociones_list = Cliente.objects.filter(categoria_id__nombre='Promociones')
    context = {
        'promociones_list': promociones_list
    }
    return render(request, 'cliente/promociones.html', context)


def home(request):
    return render(request, "cliente/index.html")

def editar_cliente(request):
    return render(request, "cliente/editar_producto.html")





def gin(request):
    productos_gin = Cliente.objects.filter(categoria_id__nombre='Gin Artesanal')
    context = {
        'productos_gin': productos_gin
    }
    return render(request, 'producto/gin.html', context)



class ClienteCategoriaList(ListView):
    model = models.ClienteCategoria


    def get_queryset(self) -> QuerySet:
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.ClienteCategoria.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.ClienteCategoria.objects.all()
        return object_list


class ClienteCategoriaCreate(CreateView):
    model = models.ClienteCategoria
    form_class = forms.ClienteCategoriaForm
    success_url = reverse_lazy("cliente:home")



class ClienteCategoriaUpdate(UpdateView):
    model = models.ClienteCategoria
    form_class = forms.ClienteCategoriaForm
    success_url = reverse_lazy("cliente:clientecategoria_list")




class ClienteCategoriaDetail(DetailView):
    model = models.ClienteCategoria
    




class ClienteCategoriaDelete(LoginRequiredMixin, DeleteView):
    model = models.ClienteCategoria
    
    success_url = reverse_lazy("cliente:clientecategoria_list")


# ***Cliente


class ClienteList(ListView):
    model = models.Cliente

    def get_queryset(self) -> QuerySet:
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.Cliente.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.Cliente.objects.all()
        return object_list


class ClienteCreate(CreateView):
    model = models.Cliente
    form_class = forms.ClienteForm
    success_url = reverse_lazy("cliente:home")


class ClienteUpdate(UpdateView):
    model = models.Cliente
    form_class = forms.ClienteForm
    success_url = reverse_lazy("cliente:cliente_list")


class ClienteDetail(DetailView):
    model = models.Cliente


class ClienteDelete(LoginRequiredMixin, DeleteView):
    model = models.Cliente
    success_url = reverse_lazy("cliente:cliente_list")


