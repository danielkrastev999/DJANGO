from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

class InicioView(TemplateView):
    template_name = "core/portada.html"