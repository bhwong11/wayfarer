from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse

# Create your views here.


class Home(TemplateView):
    template_name = 'home.html'

class Profile(TemplateView):
    template_name = 'profile.html'