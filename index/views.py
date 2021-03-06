from django.shortcuts import get_object_or_404,redirect
from django.urls.base import reverse_lazy
from .models import Message
from .forms import MessageForm
from django.views.generic import TemplateView,CreateView,ListView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
import mimetypes
from django.http import HttpResponse


#Template views:
class IndexView(TemplateView):
    template_name = "index.html"


class WorkView(TemplateView):
    template_name = "work.html"


class EducationView(TemplateView):
    template_name = "education.html"  


class ProtfolioView(TemplateView):
    template_name = "portfolio.html"


class OrthoView(TemplateView):
    template_name = "ortho.html"


class WeatherView(TemplateView):
    template_name = "weather.html"


class TodoView(TemplateView):
    template_name = "todo.html"


class SudokuView(TemplateView):
    template_name = "sudoku.html"


class ThanksMessageView(TemplateView):
    template_name = "thanks_message.html"


# List / Create / Delete Views:

class MessagesListView(LoginRequiredMixin,ListView):
    model = Message
    template_name = "my_messages.html"
    login_url = '/login/'


    def get_queryset(self):
        return Message.objects.all().order_by('read')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the counts of read and unread messages
        context['count_read'] = Message.objects.filter(read = 'True').count()
        context['count_unread'] = Message.objects.filter(read = 'False').count()
        return context    

class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = "contact.html"
    success_url = reverse_lazy("index:thanks_message")


class MessageDelete(DeleteView,LoginRequiredMixin):
    model = Message
    success_url = reverse_lazy('index:my_messages')
    login_url = '/login/'


#Function based views:

def download_cv(request):
    cv_path = "index\Curriculum.pdf"
    cv_name = "Curriculum"

    with open(cv_path, 'r') as cv:
        mime_type = mimetypes.guess_type(cv_path)
        response = HttpResponse(cv, headers={
        'Content-Type': mime_type,
        'Content-Disposition': 'attachment; filename="{}"'.format(cv_name)})
    
    return response


def message_read(request,pk):
    message = get_object_or_404(Message,pk=pk)
    message.is_read()
    message.save()
    return redirect('index:my_messages')        