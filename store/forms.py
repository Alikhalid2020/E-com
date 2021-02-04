from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product
from django.contrib.auth.forms import UserCreationForm


class CostumerForms(forms.ModelForm):
    class Meta:
        model=Project
        fields=['name', 'image', 'description', 'category', 'price']