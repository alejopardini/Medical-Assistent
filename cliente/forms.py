from django import forms

from . import models

class ClienteCategoriaForm(forms.ModelForm):
    class Meta:
        model = models.ClienteCategoria
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
        }


class ClienteForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
            "unidad_medida": forms.TextInput(attrs={"class": "form-control"}),
            "precio": forms.TextInput(attrs={"class": "form-control"}),
            "categoria_id": forms.Select(attrs={"class": "form-control"}),
            "fecha_actualizacion": forms.TextInput(attrs={"class": "form-control"}),
        }