from django import forms
from .models import Fiscalizacion, Reporte
from proyectos.models import Proyecto
from usuarios.models import Usuario
from services.utils.validators import validar_tamano_archivo


class FiscalizacionForm(forms.ModelForm):

    # Objetos referenciados
    proyecto = forms.ModelChoiceField(
        queryset=Proyecto.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Proyecto'
    )

    usuario = forms.ModelChoiceField(
        queryset=Usuario.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Usuario'
    )

    class Meta:
        model = Fiscalizacion
        fields = '__all__'

    def clean_foto(self):
        foto = self.cleaned_data.get('foto')
        return validar_tamano_archivo(foto, 100)
    
    
class ReporteForm(forms.ModelForm):
    fiscalizacion = forms.ModelChoiceField(
        queryset=Fiscalizacion.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Fiscalizacion'
    )

    class Meta:
        model = Reporte
        fields = '__all__'