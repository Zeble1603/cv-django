from django.shortcuts import render
from django.utils import timezone
from .models import Recommendation
from .forms import RecommendationForm
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recommendation

# Create your views here.


class RecoCreateView(CreateView):
    model = Recommendation
    template_name = "reco_create.html"
    form_class = RecommendationForm


class ValidRecoListView(ListView):
    model = Recommendation
    template_name = "validreco_list.html"

    def get_queryset(self):
        return super().get_queryset().filter(publish_date__lte=timezone.now()).order_by("-publish_date")

class RecoUpdateView(LoginRequiredMixin,UpdateView):
    pass

class RecoListView(LoginRequiredMixin,ListView):
    pass

class RecoDeleteView(LoginRequiredMixin,DeleteView):
    pass



