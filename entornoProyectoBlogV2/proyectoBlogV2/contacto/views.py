from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactoForm
from django.core.mail import EmailMessage

# Create your views here.
def contacto(request):
    contacto_form = ContactoForm()

    if(request.method=='POST'):
        # request tiene un diccionario POST del que puedo sacar el contenido del formulario
        nom = request.POST.get('nombre') # nombre es la variable que he creado en 'forms.py'
        cor = request.POST.get('correo')
        cont = request.POST.get('contenido')

        # Enviar un correo con el mensaje recibido a atencionCliente@miempresa.com
        #   Crear el objeto para enviar el correo
        emailEnviar = EmailMessage(
            'Nuevo mensaje de contacto',# asunto
            f'-De: {nom}\n-Email: {cor}\n\n Escribió: \n {cont}',# cuerpo
            'nocontestar@example.com', #email de origen
            ['atencionCliente@example.com'], #Lista de emails
            reply_to=[cor],# responder a 
            bcc=["atencionCliente1@miempresa.com","atencionCliente2@miempresa.com"] # solo funciona pagando
        )
        try:
            emailEnviar.send()
        except Exception as e:
            # Manejo de errores
            print(f"Error al enviar el correo: {e}")

        # data es un diccionario
        contacto_form = ContactoForm(data=request.POST)
        # redirect con tag = ok y en el html lo comprobare para sacar un mensaje
        return redirect(reverse('contacto')+'?ok')

    return render(request,"contacto/contacto.html",{
        'formulario':contacto_form
    })