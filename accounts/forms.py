from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from .models import CustomUser, Description, Locations

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')




class DescriptionForm(ModelForm):
    class Meta:
        model = Description
        fields = ['your_description']

class LocationForm(ModelForm):
    class Meta:
        model = Locations
        fields = ['input_location']