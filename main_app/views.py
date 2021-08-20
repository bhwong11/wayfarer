from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from .models import Profile
# Create your views here.


class Home(TemplateView):
    template_name = 'home.html'


class HomeError(TemplateView):
    template_name = 'home_error.html'


class UserProfile(View):
    template_name = 'profile.html'

    def get(self, request):

        return redirect(f"/profile/{request.user.id}")


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
            context = {'form': form}
            return render(request, 'registration/signup.html', context)


class ProfileUpdate(View):

    def post(self, request, pk):

        profile = Profile.objects.get(pk=pk)
        profile.image = request.POST.get("image")
        profile.current_city = request.POST.get("current_city")
        profile.save()

        user = User.objects.get(pk=request.user.id)
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.save()

        return redirect(f"/profile/{profile.pk}")

    def get(self, request, pk):

        return render(request, 'profile_update.html')


class PostDetails(DetailView):
    pass
