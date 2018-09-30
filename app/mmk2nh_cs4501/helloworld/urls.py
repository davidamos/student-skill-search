# helloworld/urls.py 
from django.conf.urls import url, include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from helloworld import views
from helloworld.views import CreateInventoryView


urlpatterns = [
	path('', views.index, name='index'),
	url(r'^inventory/$', CreateInventoryView.as_view(), name="create"),
]
urlpatterns = format_suffix_patterns(urlpatterns)