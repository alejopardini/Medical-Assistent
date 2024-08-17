from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'nombre', 'apellido', 'email', 'celular', 'historia_clinica',
            'archivo', 'fecha_inicio', 'ultima_consulta', 'fecha_nacimiento',
            'discapacidad', 'discapacidad_detalle'
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
            'historia_clinica': forms.Textarea(attrs={'class': 'form-control'}),
            'archivos': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'fecha_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'ultima_consulta': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'discapacidad_detalle': forms.Textarea(attrs={'class': 'form-control'}),
        }
