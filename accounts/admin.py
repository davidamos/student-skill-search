# users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Course

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]

    #Necessary to make extra fields visibile in admin
    fieldsets = (
        (('User'), {'fields': ('username', 'email', 'is_searching', 'image')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Course)
