from django import forms 
from .models import *
from django.contrib.auth.forms import UserCreationForm

class ContactoForms(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'

class ProductoForms(forms.ModelForm):

    class Meta:
        model = Panesbd
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    pass