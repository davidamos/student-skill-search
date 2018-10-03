# helloworld/views.py
from __future__ import unicode_literals
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.forms.models import model_to_dict
from helloworld.models import Shoe, User, Transactions, Inventory
from helloworld.serializers import ShoeSerializer, UserSerializer, TransactionsSerializer, InventorySerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.core import serializers
import os
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def _error_response(request, error_msg, error_specific=None):
	if error_specific:
		return JsonResponse({'ok': False, 'error': error_msg, 'error_info': error_specific})
	else:
		return JsonResponse({'ok': False, 'error': error_msg})

def _success_response(request, resp=None):
	if resp:
		return JsonResponse({'ok': True, 'resp': resp})
	else:
		return JsonResponse({'ok': True})

@csrf_exempt
def index(request):
	return HttpResponse('Hello, World!')

#
#	INVENTORY
#
@csrf_exempt
def inventory_views_all(request):
	i = Inventory.objects.all()
	return JsonResponse(serializers.serialize('json', i), safe=False)
@csrf_exempt
def inventory_views_create(request):
	if request.method != 'POST':
		return _error_response(request, "Registration must make POST request.")
	inventory = request.POST.dict()
	i = Inventory.objects.create(shoeIndex=inventory['shoeIndex'], quantity=inventory['quantity'], 
								 owner=inventory['owner'])
	i.save()
	return _success_response(request, {'shoeIndex': i.shoeIndex, 'quantity': i.quantity, 'owner':i.owner})
@csrf_exempt
def inventory_views_read(request, pk):
	inventory = Inventory.objects.get(id=pk)
	return JsonResponse(model_to_dict(inventory))
@csrf_exempt
def inventory_views_update(request, pk):
	i = Inventory.objects.get(id=pk)
	context = {}
	if request.method == 'POST':
		return HttpResponse(json.dumps(context), content_type="application/json")
	else:
		return JsonResponse(serializers.serialize('json', i), safe=False)
@csrf_exempt
def inventory_views_delete(request, pk):
	inventory = Inventory.objects.get(id=pk).delete()
	return HttpResponseRedirect('')

#
#	SHOE
#
@csrf_exempt
def shoe_views_all(request):
	s = Shoe.objects.all()
	return JsonResponse(serializers.serialize('json', s), safe=False)
@csrf_exempt
def shoe_views_create(request):
	if request.method != 'POST':
		return _error_response(request, "Registration must make POST request.")
	shoe = request.POST.dict()
	s = Shoe.objects.create(shoeID=shoe['shoeID'], name=shoe['name'], typeID=shoe['typeID'], 
							brand=shoe['brand'], price=shoe['price'], tradable=shoe['tradable'],
							sellable=shoe['sellable'], userID=shoe['userID'])
	s.save()
	return _success_response(request, {'shoeID': s.shoeID, 'name': s.name, 'typeID': s.typeID, 
									   'brand': s.brand, 'price': s.price, 'tradable': s.tradable,
									   'sellable': s.sellable, 'userID': s.userID})
@csrf_exempt
def shoe_views_read(request, pk):
	shoe = Shoe.objects.get(id=pk)
	return JsonResponse(model_to_dict(shoe))
@csrf_exempt
def shoe_views_update(request, pk):
	s = Shoe.objects.get(id=pk)
	context = {}
	if request.method == 'POST':
		return HttpResponse(json.dumps(context), content_type="application/json")
	else:
		return JsonResponse(serializers.serialize('json', s), safe=False)
@csrf_exempt
def shoe_views_delete(request, pk):
	shoe = Shoe.objects.get(id=pk).delete()
	return HttpResponseRedirect('')

#
#	Transactions
#
@csrf_exempt
def transactions_views_all(request):
	t = Transactions.objects.all()
	return JsonResponse(serializers.serialize('json', t), safe=False)
@csrf_exempt
def transactions_views_create(request):
	if request.method != 'POST':
		return _error_response(request, "Registration must make POST request.")
	tran = request.POST.dict()
	t = Transactions.objects.create(transactionID=tran['transactionID'], 
									transactionDate=tran['transactionDate'], 
									transactionType=tran['transactionType'], 
									sellerID=tran['sellerID'], buyerID=tran['buyerID'], 
									value=tran['value'])
	t.save()
	return _success_response(request, {'transactionID': t.transactionID, 
									   'transactionDate': t.transactionDate, 
									   'transactionType': t.transactionType, 
									   'sellerID': t.sellerID, 'buyerID': t.buyerID, 
									   'value': t.value})
@csrf_exempt
def transactions_views_read(request, pk):
	tran = Transactions.objects.get(id=pk)
	return JsonResponse(model_to_dict(tran))
@csrf_exempt
def transactions_views_update(request, pk):
	t = Transactions.objects.get(id=pk)
	context = {}
	if request.method == 'POST':
		return HttpResponse(json.dumps(context), content_type="application/json")
	else:
		return JsonResponse(serializers.serialize('json', t), safe=False)
@csrf_exempt
def transactions_views_delete(request, pk):
	t = Transactions.objects.get(id=pk).delete()
	return HttpResponseRedirect('')

#
#	Users
#
@csrf_exempt
def user_views_all(request):
	u = User.objects.all()
	return JsonResponse(serializers.serialize('json', u), safe=False)
@csrf_exempt
def user_views_create(request):
	if request.method != 'POST':
		return _error_response(request, "Registration must make POST request.")
	user = request.POST.dict()
	u = User.objects.create(userID=user['userID'], 
							name=user['name'], 
							rating=user['rating'], 
							shoesOwned=user['shoesOwned'])
	u.save()
	return _success_response(request, {'userID': u.userID, 
									   'name': u.name, 
									   'rating': u.rating, 
									   'shoesOwned': u.shoesOwned})
@csrf_exempt
def user_views_read(request, pk):
	user = User.objects.get(id=pk)
	return JsonResponse(model_to_dict(user))
@csrf_exempt
def user_views_update(request, pk):
	u = User.objects.get(id=pk)
	context = {}
	if request.method == 'POST':
		return HttpResponse(json.dumps(context), content_type="application/json")
	else:
		return JsonResponse(serializers.serialize('json', u), safe=False)
@csrf_exempt
def user_views_delete(request, pk):
	u = User.objects.get(id=pk).delete()
	return HttpResponseRedirect('')


