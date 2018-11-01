# helloworld/forms.py
from django import forms
from django.forms import ModelForm
from .models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['firstName', 'lastName', 'username', 'password']

class UserFormCheckUser(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']