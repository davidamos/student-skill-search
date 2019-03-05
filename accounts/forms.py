from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Course

from django.forms import ModelForm

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')

class CustomProfileCreationForm(forms.ModelForm):

    class Meta(forms.ModelForm):
        model = CustomUser
        fields = ('description', 'availability', 'location', 'phone_number', 'profile_email', 'home_address', 'qualities')
        
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CourseForm(forms.ModelForm):

	class Meta:
		model = Course
		fields = '__all__'
