# accounts/views.py
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from .forms import CourseForm

from .forms import CustomUserCreationForm, CustomProfileCreationForm
from .models import CustomUser, Class
from datetime import datetime
from datetime import timedelta
from django.utils import timezone

import operator



class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def all_courses(request):
	results = Class.objects.all()
	return render(request, 'accounts/all_courses.html', {'results': results})

def add_course(request):
	for i in request.POST.getlist('course'):
		course = Class.objects.get(pk=i)
		request.user.courses.add(course)
	return redirect('profile')

def list_majors(request):
	return render(request, 'accounts/list_majors.html')


def specified_major(request, course_code):
	results = Class.objects.filter(course_code__contains=course_code).order_by('course_code')
	return render(request, 'accounts/all_courses.html', {'results':results})

	

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
			request.user.courses.add(course)
			return redirect('profile')
	else:
		form = CourseForm()
	return render(request, 'accounts/course_form.html', {'form': form})
	

class ProfileView(TemplateView):
	template_name = 'accounts/profile.html'

	def get(self, request):
		form = CustomProfileCreationForm(initial={'name': request.user.name, 'description': request.user.description, 'availability': request.user.availability, 'location': request.user.location, 'phone_number': request.user.phone_number, 'profile_email': request.user.profile_email, 'home_address': request.user.home_address, 'qualities':request.user.qualities})
		return render(request, self.template_name, {'form': form})
	def post(self, request):
		form = CustomProfileCreationForm(request.POST)
		if form.is_valid():
			form.save(commit=False)
			request.user.name = request.POST['name']
			request.user.description = request.POST['description']
			request.user.availability = request.POST['availability']
			request.user.location = request.POST['location']
			#Phone Number
			request.user.phone_number = request.POST['phone_number']
			#if request.user.phone_number.isdigit() & (len(request.user.phone_number) == 10):
				#print(request.user.phone_number)
				#pass
			#else:
				#request.user.phone_number = "";
				#print("Please enter a valid number")
				
			request.user.profile_email = request.POST['profile_email']
			request.user.home_address = request.POST['home_address']
			request.user.qualities = request.POST['qualities']
			request.user.save()
			return render(request, 'accounts/user-profile.html', {'customuser':request.user})
		return render(request, self.template_name, {'form': form, 'text': text})

class HomeView(TemplateView):
	template_name = 'home.html'
	def get(self, request):
		compat = []
		if request.user.is_authenticated:
			signifier = 0
			for u in CustomUser.objects.all():
				for c1 in request.user.courses.all():
					for c2 in u.courses.all():
						if c1.course_code == c2.course_code:
							if u.username == request.user.username:
								signifier = 1
								break
							compat.append(u)
							signifier = 1
							break
					if signifier == 1:
						signifier = 0
						break
		return render(request, self.template_name, {'compat': compat, 'customuser': request.user})

class UserProfileView(TemplateView):
	template_name = 'accounts/user-profile.html'
	def get(self, request):
		return render(request, self.template_name, {'customuser': request.user})

class DetailView(generic.DetailView):
    model = CustomUser
    template_name = 'accounts/user-profile.html'

class SearchView(generic.ListView):
	
	template_name = 'accounts/search.html'
	context_object_name = 'search_list'

	def get_queryset(self):
		result = CustomUser.objects.order_by('username')
		query = self.request.GET.get('searchterm')
		query = query.replace(" ","")
		resultslist = [query]
		if query:
			query_list = query.split()
			for u in result:
				if u.is_searching == True:
					if (query.lower() in u.name.lower() or query.lower() in u.username.lower()) or (query.lower() in u.description.lower()) or (query.lower() in u.qualities.lower()) or (query.lower() in u.location.lower()) or (query.lower() in u.phone_number.lower()) or (query.lower() in u.profile_email.lower()) or (query.lower() in u.availability.lower()) or (query.lower() in u.home_address.lower()):
						resultslist.append(u)
					else:
						for course in u.courses.all():
							c = course.course_code
							c = c.replace(" ", "")
							if query.lower() in c.lower():
								resultslist.append(u)
								break
			#result = result.filter(username=query) or result.filter(description=query)
		return resultslist
		#return CustomUser.objects.order_by('username')