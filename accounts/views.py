# accounts/views.py
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect, render
from .forms import CourseForm

from .forms import CustomUserCreationForm
from .models import CustomUser
from datetime import datetime

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def post_course(request):
	if request.method == 'POST':
		print(request.POST)
		form = CourseForm(request.POST)
		if form.is_valid():
			course = form.save(commit=False)
			print(course.course_start_time)
			start_time = request.POST['course_start_time']
			end_time = request.POST['course_end_time']
			course.course_start_time = datetime.strptime(start_time, '%H:%M')
			course.course_end_time = datetime.strptime(end_time, '%H:%M')
			print(course.course_start_time)
			print(type(course.course_start_time))
			print(course)
			course.save()
			request.user.courses.add(course)
			return redirect('profile')
	else:
		form = CourseForm()
	return render(request, 'accounts/course_form.html', {'form': form})


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'accounts/profile.html')
    else:
        return redirect("{% url 'login' %}")