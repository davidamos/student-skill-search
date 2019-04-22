from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Class

from django.forms import ModelForm

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')

class CustomProfileCreationForm(forms.ModelForm):

    class Meta(forms.ModelForm):
        model = CustomUser
        fields = ('name', 'description', 'availability', 'location', 'phone_number', 'profile_email', 'home_address', 'qualities')
        is_searching = forms.BooleanField(required=False, label='Is searching:')
        
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CourseForm(forms.ModelForm):

	class Meta:
		model = Class
		fields = '__all__'

