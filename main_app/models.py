from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Model, CharField, ManyToManyField, ImageField, OneToOneField, TextField, DateTimeField, ForeignKey, SlugField
from django.db.models.deletion import CASCADE
from django.db.models.fields import IntegerField
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    image = CharField(
        max_length=500, default='https://t3.ftcdn.net/jpg/03/46/83/96/360_F_346839683_6nAPzbhpSkIpb8pmAwufkC7c5eD7wYws.jpg')
    current_city = CharField(max_length=300)

    def __str__(self):
        return self.user.username


class City(Model):
    name = CharField(max_length=300)
    image = CharField(max_length=500)
    country = CharField(max_length=300)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('city_detail', kwargs={'slug': self.slug})


class Post(Model):
    title = CharField(max_length=200)
    content = TextField(max_length=2000)
    image = CharField(max_length=500)
    created_at = DateTimeField(auto_now_add=True)
    users = ForeignKey(User, on_delete=CASCADE, related_name='posts')
    cities = ForeignKey(City, on_delete=CASCADE, related_name='posts')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']


class Comment(Model):
    title = CharField(max_length=200)
    content = TextField(max_length=1000)
    created_at = DateTimeField(auto_now_add=True)
    users = ForeignKey(User, on_delete=CASCADE, related_name='comments')
    post = ForeignKey(Post, on_delete=CASCADE, related_name='posts')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']
