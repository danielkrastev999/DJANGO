from django import forms

# Estructura parecida a models y views en registration
# Esto me permite modificar campos del formulario PARA SIEMPRE
class ContactoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'value': 'pepe'}
    ))
    correo = forms.EmailField(label="Correo", required=True, widget=forms.EmailInput(
        attrs={'class':'form-control', 'value': 'pepe@example.com'}
    ))
    contenido = forms.CharField(label="Contenido", required=True, widget=forms.Textarea(
        attrs={'class':'form-control','placeholder':'Escriba aqui su mensaje...'}
    ),min_length=10,max_length=200)
    # Que compruebe cuando llegue al servidor si tiene minimo 10 caracteres y max 200