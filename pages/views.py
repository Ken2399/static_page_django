from django.shortcuts import render

# pages/views.py

from django.views.generic import TemplateView

class ProductPageView(TemplateView):
    template_name = 'product.html'
    
class AboutPageView(TemplateView):
    template_name = 'about.html'