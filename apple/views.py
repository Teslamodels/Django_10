from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class Steve(TemplateView):
    template_name = 'index.html'
    
class Jobs(TemplateView):
    template_name = 'apple.html'
    