from django import forms
from .models import Paciente, Turno, Profesional
from datetime import datetime, time, timedelta
import pytz

class ProfesionalForm(forms.ModelForm):
    class Meta:
        model = Profesional
        fields = ['nombre', 'especialidad']

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'telefono', 'email', 'historial']

class TurnoForm(forms.ModelForm):
    TIPO_TURNO = [
        ('primera_vez', 'Primera vez (20 minutos)'),
        ('chequeo', 'Chequeo (10 minutos)'),
        ('reactivacion', 'Reactivación (15 minutos)'),
    ]
    
    tipo_turno = forms.ChoiceField(choices=TIPO_TURNO)
    profesional = forms.ModelChoiceField(queryset=Profesional.objects.all())
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    hora = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = Turno
        fields = ['paciente', 'fecha', 'hora', 'tipo_turno', 'profesional', 'descripcion', 'estado']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha'].widget.attrs.update({
            'min': datetime.now(pytz.timezone('America/Argentina/Buenos_Aires')).strftime('%Y-%m-%d'),
        })

    def clean(self):
        cleaned_data = super().clean()
        fecha = cleaned_data.get('fecha')
        hora = cleaned_data.get('hora')
        tipo_turno = cleaned_data.get('tipo_turno')

        if not fecha or not hora:
            raise forms.ValidationError("Debes seleccionar tanto la fecha como la hora.")

        fecha_hora = datetime.combine(fecha, hora)

        if fecha_hora.weekday() >= 5:  # Fin de semana
            raise forms.ValidationError("Los turnos solo se pueden agendar de lunes a viernes.")
        if not (time(8, 0) <= hora <= time(12, 0) or time(14, 0) <= hora <= time(18, 0)):
            raise forms.ValidationError("Los turnos deben estar entre 8:00-12:00 o 14:00-18:00.")
        
        if Turno.objects.filter(fecha=fecha, hora=hora).exists():
            raise forms.ValidationError("Ya existe un turno en este horario.")

        if tipo_turno == 'primera_vez':
            cleaned_data['duracion'] = timedelta(minutes=20)
        elif tipo_turno == 'chequeo':
            cleaned_data['duracion'] = timedelta(minutes=10)
        elif tipo_turno == 'reactivacion':
            cleaned_data['duracion'] = timedelta(minutes=15)

        return cleaned_data
