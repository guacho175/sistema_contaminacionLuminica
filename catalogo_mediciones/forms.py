from django import forms
from .choices import cumplimiento
from .models import Inspector, Medicion, InstrumentoMedicion


class MedicionForm(forms.ModelForm):
    cumplimiento = forms.CharField(
        widget=forms.Select(choices=cumplimiento),
        label='Cumplimiento'
    )
    latitud = forms.FloatField(
        widget=forms.NumberInput(attrs={'step': 'any', 'class': 'form-control', 'placeholder': 'Ingrese latitud'}),
        label='Latitud'
    )
    longitud = forms.FloatField(
        widget=forms.NumberInput(attrs={'step': 'any', 'class': 'form-control', 'placeholder': 'Ingrese longitud'}),
        label='Longitud'
    )
    temperatura = forms.FloatField(
        widget=forms.NumberInput(attrs={'step': 'any', 'class': 'form-control', 'placeholder': 'Ingrese temperatura'}),
        label='Temperatura (°C)'
    )
    humedad = forms.FloatField(
        required=False,
        widget=forms.NumberInput(attrs={'step': 'any', 'class': 'form-control', 'placeholder': 'Ingrese humedad'}),
        label='Humedad (%)'
    )
    valor_medido = forms.FloatField(
        widget=forms.NumberInput(attrs={'step': 'any', 'class': 'form-control', 'placeholder': 'Ingrese valor medido'}),
        label='Valor medido'
    )
    observacion = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'Ingrese observación'}),
        label='Observación'
    )

    # Objetos referenciados
    inspector = forms.ModelChoiceField(
        queryset=Inspector.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Inspector'
    )
    instrumento_medicion = forms.ModelChoiceField(
        queryset=InstrumentoMedicion.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Instrumento de Medición'
    )

    class Meta:
        model = Medicion
        fields = '__all__'










