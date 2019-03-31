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

import operator


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
			'''Need to check if start time is before end time'''
			start_time = datetime.strptime(request.POST['course_start_time'], '%H:%M')
			end_time = datetime.strptime(request.POST['course_end_time'], '%H:%M')
			if start_time < end_time:
				course.course_start_time = start_time
				course.course_end_time = end_time
			else:
				course.course_start_time = start_time
				course.course_end_time = end_time + timedelta(hours=12)
			course.save()
			print(request.user)
			print(request.user.courses.all())
			request.user.courses.add(course)
			return redirect('profile')
	else:
		form = CourseForm()
	return render(request, 'accounts/course_form.html', {'form': form})


def profile(request):
    if request.user.is_authenticated:
        form = CustomProfileCreationForm()
        return render(request, 'accounts/profile.html', {'form': form})
    else:
        return redirect("{% url 'login' %}")

class DetailView(generic.DetailView):
    model = CustomUser
    template_name = 'accounts/user-profile.html'

class SearchView(generic.ListView):
	
	template_name = 'accounts/search.html'
	context_object_name = 'search_list'

	def get_queryset(self):
		result = CustomUser.objects.order_by('username')
		query = self.request.GET.get('searchterm')
		resultslist = []
		if query:
			query_list = query.split()
			for u in result:
				if u.is_searching == True:
					if query.lower() in u.username or query.lower() in u.description or query.lower() in u.qualities \
					or query.lower() in u.location or query.lower() in u.phone_number or query.lower() in u.profile_email \
					or query.lower() in u.availability:
						resultslist.append(u)
					else:
						for course in u.courses.all():
							if query.lower() in course.course_code.lower():
								resultslist.append(u)
								break
			#result = result.filter(username=query) or result.filter(description=query)
		return resultslist
		#return CustomUser.objects.order_by('username')