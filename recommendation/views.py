from django.shortcuts import get_object_or_404, redirect
from django.urls.base import reverse_lazy
from django.utils import timezone
from .models import Recommendation
from .forms import RecommendationForm
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView,ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Template views: 

class ThanksTemplateView(TemplateView):
    template_name = "thanks.html"


# List views:

class ValidRecoListView(ListView):
    model = Recommendation
    template_name = "validreco_list.html"

    def get_queryset(self):
        return super().get_queryset().filter(
            publish_date__lte=timezone.now()).order_by("-publish_date")


class RecoListView(LoginRequiredMixin,ListView):
    model = Recommendation
    template_name = "reco_list.html"
    login_url = '/login/'

    def get_queryset(self):
        return super().get_queryset().filter(
            publish_date__isnull=True).order_by('-create_date')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)  
        # Add in the counts of read messages
        context['unpublished_reco'] = Recommendation.objects.filter(publish_date__isnull = True).count()
        return context 

# CRUD views : 

class RecoCreateView(CreateView):
    model = Recommendation
    form_class = RecommendationForm
    template_name = "reco_create.html"
    success_url = reverse_lazy('reco:thanks')
    

class RecoDetailView(LoginRequiredMixin,DetailView):
    model = Recommendation
    template_name = "reco_detail.html"
    login_url = '/login/'


class RecoUpdateView(LoginRequiredMixin,UpdateView):
    model = Recommendation
    form_class = RecommendationForm
    template_name = "reco_update.html"
    redirect_field_name = "reco/reco_detail.html"
    login_url = '/login/'


class RecoDeleteView(LoginRequiredMixin,DeleteView):
    model = Recommendation
    success_url = reverse_lazy('reco:reco_list')
    login_url = '/login/'


# Function based views :

@login_required
def reco_publish(request,pk):
    reco = get_object_or_404(Recommendation,pk=pk)
    reco.publish()
    return redirect('reco:reco_list')

