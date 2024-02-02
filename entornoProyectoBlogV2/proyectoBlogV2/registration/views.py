from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django import forms
from .forms import FormularioRegistroConCorreo

# Create your views here.
class Registro(CreateView):
    # UserCreationForm es un formulario basico de django
    form_class = FormularioRegistroConCorreo
    template_name = 'registration/registro.html'

    def get_success_url(self) -> str:
        return reverse_lazy('login') + "?registroOk"
    
    # Esto me permite modificar campos del formulario EN EL MOMENTO
    def get_form(self,form_class=None):
        form = super(Registro,self).get_form() 
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2','placeholder':'Email'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2','placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2','placeholder':'Repite la contraseña'})
        
        # Eliminar los labels predeterminados
        for i in ['username','email', 'password1','password2']:
            form.fields[i].label = ""

        return form