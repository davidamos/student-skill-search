from django.shortcuts import render

# Create your views here.
# views.py
from django.http import HttpResponse

def index(request):
	return HttpResponse('Hello, World!')