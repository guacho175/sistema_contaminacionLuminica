from django import forms
from .choices import cumplimiento
from .models import Medicion, InstrumentoMedicion


class MedicionForm(forms.ModelForm):
    latitud = forms.FloatField(
        widget=forms.NumberInput(attrs={'step': 'any', 'class': 'form-control', 'placeholder': 'Ingrese latitud'}),
        label='Latitud'
    )
    longitud = forms.FloatField(
        widget=forms.NumberInput(attrs={'step': 'any', 'class': 'form-control', 'placeholder': 'Ingrese longitud'}),
        label='Longitud'
    )
    valor_medido = forms.FloatField(
        widget=forms.NumberInput(attrs={'step': 'any', 'class': 'form-control', 'placeholder': 'Ingrese valor medido'}),
        label='Valor medido'
    )
    observacion = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'Ingrese observación'}),
        label='Observación'
    )
    cumplimiento = forms.CharField(
        widget=forms.Select(choices=cumplimiento),
        label='Cumplimiento'
    )
    # Objetos referenciados
    instrumento_medicion = forms.ModelChoiceField(
        queryset=InstrumentoMedicion.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Instrumento de Medición'
    )

    class Meta:
        model = Medicion
        fields = '__all__'










