# helloworld/urls.py 
from django.urls import path
from helloworld import views


urlpatterns = [
	path('', views.index, name='index'),
]