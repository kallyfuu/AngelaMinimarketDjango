from django import forms 
from .models import *
from django.contrib.auth.forms import UserCreationForm

class ContactoForms(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'id': 'id_nombre', 'required': False}),
            'correo': forms.EmailInput(attrs={'id': 'id_correo', 'required': False}),
            'mensaje': forms.Textarea(attrs={'id': 'id_mensaje', 'required': False}),
        }

class ProductoForms(forms.ModelForm):

    class Meta:
        model = Panesbd
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    pass