from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from .models import Profile, Post, City
# Create your views here.


class Home(TemplateView):
    template_name = 'home.html'


class HomeError(TemplateView):
    template_name = 'home_error.html'


class UserProfile(View):
    template_name = 'profile.html'

    def get(self, request):

        return redirect(f"/profile/{request.user.profile.slug}")


class UpdateProfile(View):
    def get(self, request):
        return redirect(f"/profile/{request.user.id}/update")


class ProfileDetail(DetailView):
    model = Profile
    template_name = 'user_profile.html'
    context_object_name = "details"
    slug = self.kwargs.get(self.slug_url_kwarg, None)
    slug_url_kwarg = "not_slug"  # this attribute

    def get_queryset(self):
        print self.kwargs['slug']
        a = User.objects.get(slug=self.kwargs['slug'])
        # print Details.object.get()
        # print Detail.objects.filter(article__slug=self.kwargs['slug']) fails with same error
        return User.objects.filter(=a)


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
            Profile.objects.create(
                user=request.user, current_city='N/A')
            return redirect(f'/profile/{user.profile.slug}/')
        else:
            context = {'form': form}
            return render(request, "registration/signup.html", context)


class ProfileUpdate(View):

    def post(self, request, slug):

        profile = Profile.objects.get(slug=slug)
        profile.image = request.POST.get("image")
        profile.current_city = request.POST.get("current_city")
        profile.save()

        user = User.objects.get(pk=request.user.id)
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.save()

        return redirect(f"/profile/{profile.slug}")

    def get(self, request, slug):

        return render(request, 'profile_update.html')


class PostDetails(DetailView):
    model = Post
    template_name = "post_details.html"


class CityDetailView(DetailView):
    model = City
    template_name = 'city_detail.html'
