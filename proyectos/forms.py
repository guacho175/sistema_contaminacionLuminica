from django import forms
from .choices import tipo_alumbrado, nivel_cumplimiento
from .models import Titular, RepresentanteLegal, DetalleLuminarias,  Proyecto

class ProyectoForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese nombre'}))
    longitud = forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese longitud'}))
    latitud = forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese latitud'}))
    tipo_alumbrado = forms.CharField(widget=forms.Select(choices=tipo_alumbrado))
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'class':'form-control', 'placeholder':'Descripción'}))
    nv_cumplimiento = forms.CharField(widget=forms.Select(choices=nivel_cumplimiento))

    titular = forms.ModelChoiceField(
        queryset=Titular.objects.all(),
        empty_label="Selecciona un titular",
        widget=forms.Select(attrs={'class':'form-control'})
    )
    representante_legal = forms.ModelChoiceField(
        queryset=RepresentanteLegal.objects.all(),
        empty_label="Selecciona un representante legal",
        widget=forms.Select(attrs={'class':'form-control'})
    )
    detalle_luminarias = forms.ModelChoiceField(
        queryset=DetalleLuminarias.objects.all(),
        empty_label="Selecciona un detalle de luminaria",
        widget=forms.Select(attrs={'class':'form-control'})
    )
 
    estado = forms.IntegerField(
        widget=forms.HiddenInput(),
        initial=1
    )

    class Meta:
        model = Proyecto
        fields = '__all__'




