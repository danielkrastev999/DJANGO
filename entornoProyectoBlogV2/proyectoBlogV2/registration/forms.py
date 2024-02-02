from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Heredamos de UserCreationForm
class FormularioRegistroConCorreo(UserCreationForm):
    # Es importante que se llame como en la base de datos !!
    email = forms.EmailField(required=True, help_text='Obligatorio, 254 caracteres máximo y valido')

    # le digo el modelo que quiero usar y los campos que quiero mostrar, ademas del orden
    class Meta:
        model = User 
        fields = ('username','email','password1','password2')

    # Validar campos
    def clean_email(self):
        # Buscar si hay un correo igual, que ya existe
        correo = self.cleaned_data.get('email')

        # email es el nombre que corresponde en la BD y correo a mi variable creada
        #   Filter hace que si no encuentra un correo, no de error
        if User.objects.filter(email=correo).exists(): # exisrte este correo en la base de datos?
            raise forms.ValidationError("Este Email ya esta registrado.")
        return correo
