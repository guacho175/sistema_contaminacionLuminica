from django import forms
from .choices import tipos_alumbrado, nivel_cumplimiento
from .models import Rol, Usuario, Tipo_alumbrado_art5

class EditarMedicion(forms.ModelForm):
    class Meta:
        model = Tipo_alumbrado_art5
        fields = [
            'direccion', 'latitud', 'longitud', 'tipo', 'menor_igual_90grados',
            'mayor_90grados', 'clase_luminaria', 'emision_reflexion',
            'proteccion_especial', 'radiancia_espectral', 'emision_conjunta',
            'usuario', 'nivel_cumplimiento', 'observaciones'
        ]
        
        # Definir etiquetas para los campos del formulario
        labels = {
            'direccion': 'Ubicación',
            'latitud': 'Latitud',
            'longitud': 'Longitud',
            'tipo': 'Tipo de Alumbrado',
            'menor_igual_90grados': 'Intensidad Luminosa <= 90º',
            'mayor_90grados': 'Intensidad Luminosa > 90º',
            'clase_luminaria': 'Clase de Luminaria',
            'emision_reflexion': 'Emisión por Reflexión',
            'proteccion_especial': 'Área de Protección Especial',
            'radiancia_espectral': 'Radiancia Espectral',
            'emision_conjunta': 'Emisión Conjunta Considerada',
            'usuario': 'Inspector',
            'observaciones': 'Observaciones',
            'nivel_cumplimiento': 'Nivel de Cumplimiento'
        }
        
        # Widgets para personalizar la representación de los campos en el formulario
        widgets = {
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'latitud': forms.NumberInput(attrs={'class': 'form-control'}),
            'longitud': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(choices=tipos_alumbrado, attrs={'class': 'form-control'}),
            'menor_igual_90grados': forms.NumberInput(attrs={'class': 'form-control'}),
            'mayor_90grados': forms.NumberInput(attrs={'class': 'form-control'}),
            'clase_luminaria': forms.TextInput(attrs={'class': 'form-control'}),
            'emision_reflexion': forms.NumberInput(attrs={'class': 'form-control'}),
            'proteccion_especial': forms.Select(choices=[('SI', 'Sí'), ('NO', 'No')], attrs={'class': 'form-control'}),
            'radiancia_espectral': forms.NumberInput(attrs={'class': 'form-control'}),
            'emision_conjunta': forms.Select(choices=[('SI', 'Sí'), ('NO', 'No')], attrs={'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'nivel_cumplimiento': forms.Select(choices=nivel_cumplimiento, attrs={'class': 'form-control'})
        }

