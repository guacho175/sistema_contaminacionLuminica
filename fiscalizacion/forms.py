from django import forms
from .models import Fiscalizacion, Reporte
from proyectos.models import Proyecto
from django.contrib.auth.models import User as Usuario

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        required=True,
        label='Nombre de usuario',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        required=True,
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )



class FiscalizacionForm(forms.ModelForm):

    # Objetos referenciados
    proyecto = forms.ModelChoiceField(
        queryset=Proyecto.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Proyecto'
    )

    usuario = forms.ModelChoiceField(
        queryset=Usuario.objects.filter(is_staff=False),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Usuario'
    )

    class Meta:
        model = Fiscalizacion
        fields = '__all__'
    
    
class ReporteForm(forms.ModelForm):
    fiscalizacion = forms.ModelChoiceField(
        queryset=Fiscalizacion.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Fiscalizacion'
    )

    class Meta:
        model = Reporte
        fields = '__all__'