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
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'index'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('work/', views.WorkView.as_view(), name='work'),
    path('education/', views.EducationView.as_view(), name='education'),
    path('portfolio/', views.ProtfolioView.as_view(), name='portfolio'),
    path('ortho/', views.OrthoView.as_view(), name='ortho'),
    path('weather/', views.WeatherView.as_view(), name='weather'),
    path('todo/', views.TodoView.as_view(), name='todo'),
    path('sudoku/', views.SudokuView.as_view(), name='sudoku'),
    path('contact/', views.MessageCreateView.as_view(), name='contact'),
    path('thanks/', views.ThanksMessageView.as_view(), name='thanks_message'),
    path('dl/<str:filepath>/', views.download_cv),
    path('my_messages',views.MessagesListView.as_view(),name="my_messages"),
    path('my_messages/<pk>/read',views.message_read,name="message_read"),
    path('my_messages/<pk>/delete',views.MessageDelete.as_view(),name="message_delete"),

]
