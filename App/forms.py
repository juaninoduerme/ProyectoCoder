from email.policy import default
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Avatar
from django.db import models


class JuegosDePcFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    fechaDeLanzamiento = forms.DateField()
    genero = forms.CharField(max_length=100)
    sinopsis = forms.CharField(max_length=200)

class JuegosDeConsolaFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    fechaDeLanzamiento = forms.DateField()
    genero = forms.CharField(max_length=100)
    consola = forms.CharField(max_length=50)
    sinopsis = forms.CharField(max_length=200)

class NoticiasFormulario(forms.Form):
    titulo = forms.CharField(max_length=50)
    subtitulo = forms.CharField(max_length=100)
    cuerpo = forms.CharField(max_length=1500)


class Userregister(UserCreationForm):
    # email = forms.EmailField()
    # passw1 = forms.CharField(widget=forms.PasswordInput)
    # passw2 = forms.CharField(widget=forms.PasswordInput)
    # profile = models.ImageField(default='profile1.jpg', upload_to="profile",null=True, blank=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # help_texts = {k:"" for k in fields}


class CustomForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    last_name = forms.CharField()
    first_name = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','last_name', 'first_name','email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
