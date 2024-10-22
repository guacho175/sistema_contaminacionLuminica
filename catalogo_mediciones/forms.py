from django import forms
from .choices import tipos_alumbrado
from .models import Tipo_alumbrado_art5, Tipo_alumbrado_art6, CatalogoMedicion


class MedicionForm(forms.ModelForm):

    medicion_art5 = forms.ModelChoiceField(
        queryset=Tipo_alumbrado_art5.objects.filter(estado=0),
        required=False,
        empty_label="Selecciona una medición de tipo art5",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    medicion_art6 = forms.ModelChoiceField(
    queryset=Tipo_alumbrado_art6.objects.filter(estado=0),
    required=False,
    empty_label="Selecciona una medición de tipo art6",
    widget=forms.Select(attrs={'class': 'form-control'})
    )   

    class Meta:
        model = CatalogoMedicion
        fields = '__all__'
    
    def clean(self):
        cleaned_data = super().clean()
        medicion_art5 = cleaned_data.get("medicion_art5")
        medicion_art6 = cleaned_data.get("medicion_art6")

        # Verificar que solo uno de los dos campos esté completado
        if medicion_art5 and medicion_art6:
            raise forms.ValidationError("Solo puedes seleccionar una medición: Art. 5 o Art. 6, no ambas.")
        
        if not medicion_art5 and not medicion_art6:
            raise forms.ValidationError("Debes seleccionar una medición: Art. 5 o Art. 6.")
        
        return cleaned_data


class EditarMedicion(forms.ModelForm):
    class Meta:
        model = Tipo_alumbrado_art5
        fields = [
            'direccion', 'latitud', 'longitud', 'tipo_alumbrado', 'menor_igual_90grados',
            'mayor_90grados', 'clase_luminaria', 'emision_reflexion',
            'proteccion_especial', 'radiancia_espectral', 'emision_conjunta',
            'usuario', 'observaciones','estado'
        ]
        
        # Definir etiquetas para los campos del formulario
        labels = {
            'direccion': 'Ubicación',
            'latitud': 'Latitud',
            'longitud': 'Longitud',
            'tipo_alumbrado': 'Tipo de Alumbrado',
            'menor_igual_90grados': 'Intensidad Luminosa <= 90º',
            'mayor_90grados': 'Intensidad Luminosa > 90º',
            'clase_luminaria': 'Clase de Luminaria',
            'emision_reflexion': 'Emisión por Reflexión',
            'proteccion_especial': 'Área de Protección Especial',
            'radiancia_espectral': 'Radiancia Espectral',
            'emision_conjunta': 'Emisión Conjunta Considerada',
            'usuario': 'Inspector',
            'observaciones': 'Observaciones',
            'estado': 'Estado de medición'
        }
        
        # Widgets para personalizar la representación de los campos en el formulario
        widgets = {
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'latitud': forms.NumberInput(attrs={'class': 'form-control'}),
            'longitud': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo_alumbrado': forms.Select(choices=tipos_alumbrado, attrs={'class': 'form-control'}),
            'menor_igual_90grados': forms.NumberInput(attrs={'class': 'form-control'}),
            'mayor_90grados': forms.NumberInput(attrs={'class': 'form-control'}),
            'clase_luminaria': forms.TextInput(attrs={'class': 'form-control'}),
            'emision_reflexion': forms.NumberInput(attrs={'class': 'form-control'}),
            'proteccion_especial': forms.Select(choices=[('SI', 'Sí'), ('NO', 'No')], attrs={'class': 'form-control'}),
            'radiancia_espectral': forms.NumberInput(attrs={'class': 'form-control'}),
            'emision_conjunta': forms.Select(choices=[('SI', 'Sí'), ('NO', 'No')], attrs={'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'estado': forms.Select(choices=[('1', 'En catálogo'), ('0', 'Fuera del catálogo')], attrs={'class': 'form-control'})
        }

