from django import forms
from .choices import cumplimiento
from .models import Inspector, DetalleMedicion, Proyecto, Medicion

class MedicionForm(forms.ModelForm):

    estado = forms.IntegerField(widget=forms.HiddenInput(), initial=1)

    inspector = forms.ModelChoiceField(
        queryset=Inspector.objects.all(),
        empty_label="Selecciona inspector",
        widget=forms.Select(attrs={'class':'form-control'})
    )
    proyecto = forms.ModelChoiceField(
        queryset=Proyecto.objects.filter(estado=0),
        empty_label="Selecciona Proyecto",
        widget=forms.Select(attrs={'class':'form-control'})
    )


    class Meta:
        model = Medicion
        fields = '__all__'











