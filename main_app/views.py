from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from .models import Profile, Post, City, Comment
# Create your views here.


class Home(TemplateView):
    template_name = 'home.html'


class HomeError(TemplateView):
    template_name = 'home_error.html'


class UserProfile(View):
    template_name = 'profile.html'

    def get(self, request):

        return redirect(f"/profile/{request.user.id}")


class UpdateProfile(View):
    def get(self, request):
        return redirect(f"/profile/{request.user.id}/update")


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
            Profile.objects.create(user=request.user, current_city='N/A')
            return redirect(f'/profile/{user.profile.id}/')
        else:
            context = {'form': form}
            return render(request, "registration/signup.html", context)


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


class PostCreate(View):
    def get(self, request):
        context = {'cities': City.objects.all()}
        return render(request, 'post_create.html', context)

    def post(self, request):
        title = request.POST.get('title')
        content = request.POST.get('content')
        cities = City.objects.get(pk=request.POST.get('cities'))
        user = request.user
        new_post = Post.objects.create(
            title=title, content=content, image='https://cdn.britannica.com/68/95568-050-A0955C0F/Palace-of-Diocletian-Split-Croatia.jpg', cities=cities, users=user)
        return redirect(f"/cities/{cities.pk}")


class PostUpdate(UpdateView):
    def get(self, request, pk):
        context = {'cities': City.objects.all(
        ), 'post': Post.objects.get(pk=pk)}
        return render(request, 'post_update.html', context)

    def post(self, request, pk):
        title = request.POST.get('title')
        content = request.POST.get('content')
        cities = City.objects.get(pk=request.POST.get('cities'))
        Post.objects.filter(pk=pk).update(
            title=title, content=content, image='https://cdn.britannica.com/68/95568-050-A0955C0F/Palace-of-Diocletian-Split-Croatia.jpg', cities=cities)
        return redirect(f"/posts/{pk}")


class PostDelete(View):
    def get(self, request, pk):
        context = {'cities': City.objects.all(
        ), 'post': Post.objects.get(pk=pk)}
        return render(request, 'post_delete.html', context)

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        deletedPost = Post.objects.filter(pk=pk).delete()
        return redirect(f"/cities/{post.cities.pk}")


class PostDetails(DetailView):
    model = Post
    template_name = 'post_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.all()
        return context


class CityDetailView(DetailView):
    model = City
    template_name = 'city_detail.html'


class CityDetail(DetailView):
    model = City
    template_name = 'city_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cities'] = City.objects.all()
        return context


class CommentCreate(CreateView):
    model = Comment
    template_name = 'comment_create.html'
    fields = ['title', 'content', 'users', 'post']

    def post(self, request):
        #comment = Comment.objects.get(pk=pk)
        ##createdcomment = Comment.objects.filter(pk=pk)
        # return redirect(f"/cities/{Comment.cities.pk}")
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post.objects.get(pk=request.POST.get('post'))
        users = request.user

        new_comment = Comment.objects.create(
            title=title, content=content, post = post,users=users
        )
        return redirect(f"/posts/{new_comment.post.pk}")

class CommentUpdate(View):
    pass

class CommentDelete(View):
    pass