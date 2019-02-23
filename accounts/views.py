# accounts/views.py
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect, render

from .forms import CustomUserCreationForm
from .models import CustomUser

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'accounts/profile.html')
    else:
        return redirect("{% url 'login' %}")