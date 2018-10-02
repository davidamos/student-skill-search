# helloworld/urls.py 
from django.conf.urls import url, include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from helloworld import views
from helloworld.views import CreateUserView, CreateShoeView, CreateTransactionsView, CreateInventoryView
from helloworld.views import UserDetailsView, ShoeDetailsView, TransactionsDetailsView, InventoryDetailsView


urlpatterns = [
	path('', views.index, name='index'),
	url(r'^api/v1/inventory', CreateInventoryView.as_view()), 
	url(r'^api/v1/user', CreateUserView.as_view()), 
	url(r'^api/v1/shoe', CreateShoeView.as_view()), 
	url(r'^api/v1/transactions', CreateTransactionsView.as_view()), 
	url(r'^api/v1/inventory/(?P<pk>[0-9]+)/$', InventoryDetailsView.as_view()),
	url(r'^api/v1/user/(?P<pk>[0-9]+)/$', UserDetailsView.as_view()),
	url(r'^api/v1/shoe/(?P<pk>[0-9]+)/$', ShoeDetailsView.as_view()),
	url(r'^api/v1/transactions/(?P<pk>[0-9]+)/$', TransactionsDetailsView.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)