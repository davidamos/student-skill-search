# helloworld/urls.py 
from django.conf.urls import url, include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from helloworld import views
from helloworld.views import inventory_views_all, inventory_views_create, inventory_views_read, inventory_views_update, inventory_views_delete 
from helloworld.views import shoe_views_all, shoe_views_create, shoe_views_read, shoe_views_update, shoe_views_delete 
from helloworld.views import transactions_views_all, transactions_views_create, transactions_views_read, transactions_views_update, transactions_views_delete 
from helloworld.views import user_views_all, user_views_create, user_views_read, user_views_update, user_views_delete 

urlpatterns = [
	path('', views.index, name='index'), # HOME PAGE
	#
	# URLS FOR INVENTORY
	#
	url(r'^api/v1/inventory$', inventory_views_all),
	url(r'^api/v1/inventory/(?P<pk>[0-9]+)$', inventory_views_read), 
	url(r'^api/v1/inventory/create$', inventory_views_create), 
	url(r'^api/v1/inventory/(?P<pk>[0-9]+)/update$', inventory_views_update), 
	url(r'^api/v1/inventory/(?P<pk>[0-9]+)/delete$', inventory_views_delete),
	#
	# URLS FOR SHOE
	#
	url(r'^api/v1/shoe$', shoe_views_all),
	url(r'^api/v1/shoe/(?P<pk>[0-9]+)$', shoe_views_read), 
	url(r'^api/v1/shoe/create$', shoe_views_create), 
	url(r'^api/v1/shoe/(?P<pk>[0-9]+)/update$', shoe_views_update), 
	url(r'^api/v1/shoe/(?P<pk>[0-9]+)/delete$', shoe_views_delete),
	#
	# URLS FOR TRANSACTIONS
	#
	url(r'^api/v1/transactions$', transactions_views_all),
	url(r'^api/v1/transactions/(?P<pk>[0-9]+)$', transactions_views_read), 
	url(r'^api/v1/transactions/create$', transactions_views_create), 
	url(r'^api/v1/transactions/(?P<pk>[0-9]+)/update$', transactions_views_update), 
	url(r'^api/v1/transactions/(?P<pk>[0-9]+)/delete$', transactions_views_delete),
	#
	# URLS FOR USER
	#
	url(r'^api/v1/user$', user_views_all),
	url(r'^api/v1/user/(?P<pk>[0-9]+)$', user_views_read), 
	url(r'^api/v1/user/create$', user_views_create), 
	url(r'^api/v1/user/(?P<pk>[0-9]+)/update$', user_views_update), 
	url(r'^api/v1/user/(?P<pk>[0-9]+)/delete$', user_views_delete),
]
urlpatterns = format_suffix_patterns(urlpatterns)