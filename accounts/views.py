# accounts/views.py
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect, render
from .forms import ClassForm

from .forms import CustomUserCreationForm, CustomProfileCreationForm
from .models import CustomUser
from datetime import datetime
from datetime import timedelta
from django.utils import timezone


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def post_course(request):
	if request.method == 'POST':
		print(request.POST)
		form = ClassForm(request.POST)
		if form.is_valid():
			course = form.save(commit=False)
			'''Need to check if start time is before end time'''
			start_time = datetime.strptime(request.POST['course_start_time'], '%H:%M')
			end_time = datetime.strptime(request.POST['course_end_time'], '%H:%M')
			'''handle the case where end time is after noon and start time is before noon'''
			if start_time < end_time:
				course.course_start_time = start_time
				course.course_end_time = end_time
			else:
				course.course_start_time = start_time
				course.course_end_time = end_time + timedelta(hours=12)
			'''handle case where time is too early to be an am class'''
			if start_time < datetime.strptime('8:00', '%H:%M'):
				course.course_start_time = start_time + timedelta(hours=12)
				course.course_end_time = end_time + timedelta(hours=12)
			course.save()
			print(request.user)
			print(request.user.courses.all())
			request.user.courses.add(course)
			return redirect('profile')
	else:
		form = ClassForm()
	return render(request, 'accounts/course_form.html', {'form': form})


def profile(request):
    if request.user.is_authenticated:
        form = CustomProfileCreationForm()
        return render(request, 'accounts/profile.html', {'form': form})
    else:
        return redirect("{% url 'login' %}")
