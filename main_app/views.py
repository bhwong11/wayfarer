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

class UserProfile(TemplateView):
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


class ProfileUpdate(View):
    
    # model = Profile
    # fields = ['image', 'current_city']
    # template_name = "profile_update.html"
    # success_url = "/profile/"
    
    def post(self, request, pk):
        
        profile = Profile.objects.get(pk=pk)
        profile.image = request.POST.get("image")
        profile.save()
        
        return redirect(f"/profile/{pk}")
        # user =
    def get(self, request, pk):
        
        # context = {'form': form}
        return render(request, 'profile_update.html')
        
        # print("request", request)
    
    # def get_success_url(self):
    #     return reverse('profile', kwargs={'pk': self.object.pk})

class PostDetails(DetailView):
    pass