from django import forms
from .choices import cumplimiento, tipo_medicion
from .models import Medicion, InstrumentoMedicion
from fiscalizacion.models import Fiscalizacion
from services.utils.validators import validar_tamano_archivo



class MedicionForm(forms.ModelForm):
    tipo = forms.CharField(widget=forms.Select(choices=tipo_medicion))

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
        label='Temperatura'
    
    )
    humedad = forms.FloatField(
        widget=forms.NumberInput(attrs={'step': 'any', 'class': 'form-control', 'placeholder': 'Ingrese humedad'}),
        label='Humedad'
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
    instrumento_medicion = forms.ModelChoiceField(
        queryset=InstrumentoMedicion.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Instrumento de Medición'
    )

    fiscalizacion = forms.ModelChoiceField(
        queryset=Fiscalizacion.objects.all(),
        widget=forms.HiddenInput(),
        label='Fiscalización'
    )

    def clean_foto(self):
        foto = self.cleaned_data.get('foto')
        return validar_tamano_archivo(foto, 100)

    class Meta:
        model = Medicion
        fields = '__all__'











