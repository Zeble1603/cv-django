from django.shortcuts import render
from django.urls.base import reverse_lazy
from .models import Message
from .forms import MessageForm
from django.views.generic import TemplateView,CreateView

# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"

class WorkView(TemplateView):
    template_name = "work.html"

class EducationView(TemplateView):
    template_name = "education.html"  

class ProtfolioView(TemplateView):
    template_name = "portfolio.html" 

class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = "contact.html"
    success_url = reverse_lazy("index:thanks_message")

class ThanksMessageView(TemplateView):
    template_name = "thanks_message.html"
