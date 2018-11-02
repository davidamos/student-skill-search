# helloworld/views.py
from __future__ import unicode_literals
import json, os, hmac, datetime, base64
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, FileResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.forms.models import model_to_dict
from django.utils import timezone
from django.conf import settings
from django.contrib.auth import hashers
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from helloworld.models import Shoe, User, Transactions, Inventory
from helloworld.serializers import ShoeSerializer, UserSerializer, TransactionsSerializer, InventorySerializer
from .forms import UserForm, UserFormCheckUser


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
	return render(request, 'home.html')

#
# AUTH
#

@csrf_exempt
def login(request):
    return render(request, 'registration/login.html')
@csrf_exempt
def signup(request):
    return render(request, 'signup.html')

#
#	INVENTORY
#
@csrf_exempt
def inventory_views_all(request):
	inventory = Inventory.objects.all()
	return render(request, 'inventory.html', {'inventory':inventory})
	# return JsonResponse(serializers.serialize('json', i), safe=False)
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
	shoes = Shoe.objects.all()
	return render(request, 'shoe.html', {'shoes':shoes})
	# return JsonResponse(serializers.serialize('json', s), safe=False)
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
	transactions = Transactions.objects.all()
	return render(request, 'transactions.html', {'transactions': transactions})
	# return JsonResponse(serializers.serialize('json', t), safe=False)
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
	users = User.objects.all()
	return render(request, 'user.html', {'users': users})
	# return JsonResponse(serializers.serialize('json', u), safe=False)
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

def createAuth(request):
    if request.method == 'GET':
        # auth = Authenticator.objects.all().delete()
        auth = Authenticator.objects.filter(**request.GET.dict())
        data = serializers.serialize("json", auth)
        return JsonResponse(json.loads(data), safe=False)

    if request.method == 'POST':
        user_id = request.POST["user_id"]
        response_data = {}

        try:
            auth = Authenticator.objects.get(user_id=user_id)
        except ObjectDoesNotExist:
            authenticator = hmac.new(
                key=settings.SECRET_KEY.encode('utf-8'),
                msg=os.urandom(32),
                digestmod='sha256',
            ).hexdigest()

            theAuth = Authenticator(user_id=user_id, authenticator=authenticator)

            theAuth.save()
            response_data['result'] = '200'
            response_data['message'] = 'OK: Successful'
            response_data['auth'] = json.loads(serializers.serialize("json", [theAuth, ]))
            return JsonResponse(response_data, safe=False)
        else:
            listAuth = Authenticator.objects.filter(user_id=user_id)
            for singleAuth in listAuth:
                singleAuth.delete()

            authenticator = hmac.new(
                key=settings.SECRET_KEY.encode('utf-8'),
                msg=os.urandom(32),
                digestmod='sha256',
            ).hexdigest()
            auth.authenticator = authenticator
            auth.save()

            response_data = {}
            response_data['result'] = '200'
            response_data['message'] = 'OK: Successful'
            response_data['auth'] = json.loads(serializers.serialize("json", [auth, ]))
            return JsonResponse(response_data, safe=False)

    else:
        response_data = {}
        response_data['result'] = '400'
        response_data['message'] = 'Bad Request'
        return JsonResponse(response_data, safe=False)

def checkAuth(request):
    if request.method == 'POST':
        # user_id = request.POST["user_id"]
        token = request.POST["token"]
        response_data = {}

        try:
            auth = Authenticator.objects.get(pk=token)
        except ObjectDoesNotExist:
            response_data = {}
            response_data['result'] = '404'
            response_data['message'] = token
            return JsonResponse(response_data, safe=False)

        else:
            date = auth.date_created
            currentDate = timezone.now()
            time = (currentDate - date).seconds / 3600
            days = (currentDate - date).days
            if (time >= 1 or days > 0):
                auth.delete()
                response_data['result'] = '404'
                response_data['message'] = token
                return JsonResponse(response_data, safe=False)
            else:
                response_data['result'] = '200'
                response_data['message'] = 'OK: Successful'
                return JsonResponse(response_data, safe=False)


def removeAuth(request):
    if request.method == 'POST':
        token = request.POST['token']
        response_data = {}

        try:
            auth = Authenticator.objects.get(pk=token)
        except ObjectDoesNotExist:
            response_data['result'] = '404'
            response_data['message'] = token
            return JsonResponse(response_data, safe=False)
        else:
            auth.delete()
            response_data['result'] = '200'
            response_data['message'] = 'OK: Successful'
            return JsonResponse(response_data, safe=False)


def checkUser(request):
    if request.method == 'POST':

        response_data = {}
        form = UserFormCheckUser(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            theUser = User.objects.get(username=username)

            if (hashers.check_password(password, theUser.password)):
                response_data['result'] = '200'
                response_data['message'] = 'OK: Successful'
                response_data['user_id'] = theUser.pk
                return JsonResponse(response_data, safe=False)
            else:
                response_data['result'] = '404'
                response_data['message'] = 'Invalid User'
                return JsonResponse(response_data, safe=False)
        else:
            response_data['result'] = '400'
            response_data['message'] = 'Bad Request'
            return JsonResponse(response_data, safe=False)

def getUserByAuth(request):
    if request.method == 'POST':
        if 'token' not in request.POST:
            response_data = {}
            response_data['result'] = '404'
            response_data['message'] = "No token given"
            return JsonResponse(response_data, safe=False)
        else:
            token = request.POST["token"]
            try:
                auth = Authenticator.objects.get(pk=token)
            except ObjectDoesNotExist:
                response_data = {}
                response_data['result'] = '404'
                response_data['message'] = token
                return JsonResponse(response_data, safe=False)
            else:
                date = auth.date_created
                currentDate = timezone.now()
                time = (currentDate - date).seconds / 3600
                days = (currentDate - date).days
                if (time >= 1 or days > 0):
                    auth.delete()
                    response_data = {}
                    response_data['result'] = '404'
                    response_data['message'] = token
                    return JsonResponse(response_data, safe=False)
                else:
                    user_id = auth.user_id
                    current_user = User.objects.get(pk=user_id)
                    response_data = {}
                    response_data['result'] = '200'
                    response_data['message'] = 'OK: Successful'
                    response_data['user'] = json.loads(serializers.serialize("json", [current_user]))
                    return JsonResponse(response_data, safe=False)
