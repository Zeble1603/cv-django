from django.shortcuts import get_object_or_404, redirect, render
from django.urls.base import reverse, reverse_lazy
from django.utils import timezone
from .models import Recommendation
from .forms import RecommendationForm
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView,ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

class RecoCreateView(CreateView):
    model = Recommendation
    template_name = "reco_create.html"
    success_url = reverse_lazy('reco:thanks')
    form_class = RecommendationForm

class ThanksTemplateView(TemplateView):
    template_name = "thanks.html"


class ValidRecoListView(ListView):
    model = Recommendation
    template_name = "validreco_list.html"

    def get_queryset(self):
        return super().get_queryset().filter(publish_date__lte=timezone.now()).order_by("-publish_date")

class RecoDetailView(LoginRequiredMixin,DetailView):
    model = Recommendation
    template_name = "reco_detail.html"


class RecoUpdateView(LoginRequiredMixin,UpdateView):
    model = Recommendation
    form_class = RecommendationForm
    template_name = "reco_update.html"
    redirect_field_name = "reco/reco_detail.html"

    

class RecoListView(LoginRequiredMixin,ListView):
    model = Recommendation
    template_name = "reco_list.html"

    def get_queryset(self):
        return super().get_queryset().filter(publish_date__isnull=True).order_by('-create_date')

class RecoDeleteView(LoginRequiredMixin,DeleteView):
    model = Recommendation
    template_name = "reco_delete.html"
    success_url = reverse_lazy('reco_list')

@login_required
def reco_publish(request,pk):
    reco = get_object_or_404(Recommendation,pk=pk)
    reco.publish()
    return redirect('reco_detail',pk=pk)

