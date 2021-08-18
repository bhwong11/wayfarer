from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Model, CharField, ManyToManyField, ImageField, OneToOneField
from django.db.models.fields import IntegerField
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User

# Create your models here.


class Profile(Model):
    user = OneToOneField(User, on_delete=models.CASCADE)
    image = CharField(
        max_length=500, default='https://t3.ftcdn.net/jpg/03/46/83/96/360_F_346839683_6nAPzbhpSkIpb8pmAwufkC7c5eD7wYws.jpg')
    current_city = CharField(max_length=300)

    def __str__(self):
        return self.user.username
