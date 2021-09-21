"""cv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from cv.recommendation.views import RecoListView
from django.contrib import admin
from django.urls import path
from recommendation import views

urlpatterns = [
    path("", views.ValidRecoListView.as_view(), name="validreco_list"),
    path("reco/list", views.RecoListView.as_view(), name="reco_list"),
    path("reco/new", views.RecoCreateView.as_view(), name="reco_create"),
    path("reco/<pk>", views.RecoDetailView.as_view(), name="reco_detail"),
    path("reco/<pk>/update", views.RecoUpdateView.as_view(), name="reco_update"),
    path("reco/<pk>/delete", views.RecoDeleteView.as_view(), name="reco_delete"),
    path("reco/<pk>/publish", views.reco_publish, name="reco_publish"),

]