from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"

class WorkView(TemplateView):
    template_name = "work.html"

class EducationView(TemplateView):
    template_name = "education.html"  

class ProtfolioView(TemplateView):
    template_name = "portfolio.html" 



