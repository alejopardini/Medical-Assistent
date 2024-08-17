from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Paciente
from .forms import PacienteForm
from consultas.models import Consulta
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

def home(request):
    pacientes = Paciente.objects.all()
    return render(request, 'paciente/editar_paciente.html', {'pacientes': pacientes})

def editar_paciente(request):
    return render(request, "paciente/editar_paciente.html")

class PacienteListView(ListView):
    model = Paciente
    template_name = 'paciente/paciente_list.html'
    context_object_name = 'pacientes'

class PacienteDetailView(DetailView):
    model = Paciente
    template_name = 'paciente/paciente_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['consultas'] = Consulta.objects.filter(paciente=self.object)
        context['adjuntos'] = self.object.adjuntos.all()
        return context

class PacienteCreateView(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'paciente/paciente_form.html'
    success_url = reverse_lazy('paciente:paciente_list')

class PacienteUpdateView(UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'paciente/paciente_form.html'
    success_url = reverse_lazy('paciente:paciente_list')

class PacienteDeleteView(DeleteView):
    model = Paciente
    template_name = 'paciente/paciente_confirm_delete.html'
    success_url = reverse_lazy('paciente:paciente_list')
