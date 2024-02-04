from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# Create your models here.
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        #fields = "__all__"
        fields = ['username', 'email', 'password1', 'password2']
