from django.shortcuts import render, get_object_or_404, redirect
from .models import Turno, Profesional
from .forms import TurnoForm,ProfesionalForm


# Vista para gestionar profesionales (opcional)
def listar_profesionales(request):
    profesionales = Profesional.objects.all()
    return render(request, 'turnos/listar_profesionales.html', {'profesionales': profesionales})

def crear_profesional(request):
    if request.method == 'POST':
        form = ProfesionalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('turnos:listar_profesionales')
    else:
        form = ProfesionalForm()
    return render(request, 'turnos/crear_profesional.html', {'form': form})


def turnos(request):
    turnos = Turno.objects.all()  # O el queryset adecuado para tus turnos
    return render(request, 'turnos/turnos.html', {'turnos': turnos})

def crear_turno(request):
    if request.method == 'POST':
        form = TurnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('turnos:listar_turnos')
    else:
        form = TurnoForm()
    print("Form:", form)
    return render(request, 'turnos/crear_turno.html', {'form': form})

def listar_turnos(request):
    turnos = Turno.objects.all().order_by('fecha', 'hora')
    print("Turnos:", turnos)
    return render(request, 'turnos/listar_turnos.html', {'turnos': turnos})

def detalle_turno(request, id):
    turno = get_object_or_404(Turno, id=id)
    return render(request, 'turnos/detalle_turno.html', {'turno': turno})

def editar_turno(request, id):
    turno = get_object_or_404(Turno, id=id)
    if request.method == 'POST':
        form = TurnoForm(request.POST, instance=turno)
        if form.is_valid():
            form.save()
            return redirect('turnos:detalle_turno', id=turno.id)
    else:
        form = TurnoForm(instance=turno)
    return render(request, 'turnos/editar_turno.html', {'form': form})

def eliminar_turno(request, id):
    turno = get_object_or_404(Turno, id=id)
    if request.method == 'POST':
        turno.delete()
        return redirect('turnos:listar_turnos')
    return render(request, 'turnos/eliminar_turno.html', {'turno': turno})
