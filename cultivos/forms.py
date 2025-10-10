from django import forms
from .models import Cultivo

class CultivoForm(forms.ModelForm):
    class Meta:
        model = Cultivo
        fields = ['nombre', 'tipo', 'siembra', 'cosecha', 'zona', 'plagas']
        widgets = {
            'plagas': forms.CheckboxSelectMultiple(), #se ven como varios check
            'siembra': forms.TextInput(attrs={'placeholder':'Ej:Agosto'}),
            'cosecha': forms.TextInput(attrs={'placeholder':'Ej:Diciembre'})
        }
        labels = {
            'nombre': 'Nombre del cultivo',
            'tipo': 'Tipo de cultivo',
            'siembra': 'Epoca de siembra',
            'cosecha': 'Epoca de cosecha',
            'zona': 'Zona Asignada',
            'plagas': 'Plagas asociadas'
        }