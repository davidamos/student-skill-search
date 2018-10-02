# helloworld/urls.py 
from django.conf.urls import url, include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from helloworld import views
from helloworld.views import CreateInventoryView, InventoryDetailsView


urlpatterns = [
	path('', views.index, name='index'),
	url(r'^api/v1/inventory', CreateInventoryView.as_view()), 
	url(r'^api/v1/inventory/(?P<pk>[0-9]+)/$', InventoryDetailsView.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)