from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

# Create your views here.


class Home(TemplateView):
    template_name = 'home.html'


class HomeError(TemplateView):
    template_name = 'home_error.html'

class Profile(TemplateView):
    template_name = 'profile.html'


class ProfileDetail(DetailView):
    model = User
    template_name = 'user_profile.html'


class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'registration/signup.html', context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
            # change this to user_edit html
        else:
            context = {'form': form}
            return render(request, 'registration/signup.html', context)


class ProfileUpdate(UpdateView):
    pass

class PostDetails(DetailView):
    pass