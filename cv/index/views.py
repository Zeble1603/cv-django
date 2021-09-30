from django.shortcuts import render
from django.urls.base import reverse_lazy
from .models import Message
from .forms import MessageForm
from django.views.generic import TemplateView,CreateView
import mimetypes
from django.http import HttpResponse

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

def download_cv(request):
    cv_path = "index\Curriculum Blaise 2021.pdf"
    cv_name = "Curriculum Blaise 2021.pdf"

    with open(cv_path, 'r') as cv:
        mime_type, _ = mimetypes.guess_type(cv_path)
        response = HttpResponse(cv, headers={
        'Content-Type': mime_type,
        'Content-Disposition': 'attachment; filename="{}"'.format(cv_name),})
    