from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

from django.forms import ModelForm
from django import forms


class UploadForm(ModelForm):
    message = forms.Textarea()
    file = forms.FileField()

    class Meta:
        model = Audio
        fields = ['name','message', 'file']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
