from django import forms
from .models import TipoAlumbradoArt5, TipoAlumbradoArt6, CatalogoMedicion # Agregamos los modelos para traer sus atributos como campos


class MedicionForm(forms.ModelForm):
    # Declaramos los campos, sus tipos y atributos para el formulario

    # Declaramos los campos que seran un registro de una tabla
    medicion_art5 = forms.ModelChoiceField(
        queryset=TipoAlumbradoArt5.objects.filter(estado=0),
        required=False,
        empty_label="Selecciona una medición de tipo art5",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    medicion_art6 = forms.ModelChoiceField(
    queryset=TipoAlumbradoArt6.objects.filter(estado=0),
    required=False,
    empty_label="Selecciona una medición de tipo art6",
    widget=forms.Select(attrs={'class': 'form-control'})
    )   

    class Meta:
        model = CatalogoMedicion
        fields = '__all__' # Todos los campos serán incluios
    
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



