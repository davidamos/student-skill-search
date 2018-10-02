# helloworld/views.py
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from helloworld.models import Shoe, User, Transactions, Inventory
from helloworld.serializers import ShoeSerializer, UserSerializer, TransactionsSerializer, InventorySerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

# Create your views here.

def index(request):
	return HttpResponse('Hello, World!')

class CreateInventoryView(generics.ListCreateAPIView):
	"""
	API endpoint that allows Inventory to be viewed or edited.
	"""
	queryset = Inventory.objects.all()
	serializer_class = InventorySerializer
	def perform_create(self, serializer):
		"""Save the post data when creating a new bucketlist."""
		serializer.save()

class InventoryDetailsView(generics.RetrieveUpdateDestroyAPIView):
	"""This class handles the http GET, PUT and DELETE requests."""
	queryset = Inventory.objects.all()
	serializer_class = InventorySerializer

class CreateUserView(generics.ListCreateAPIView):
	"""
	API endpoint that allows Users to be viewed or edited.
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer
	def perform_create(self, serializer):
		"""Save the post data when creating a new bucketlist."""
		serializer.save()

class UserDetailsView(generics.RetrieveUpdateDestroyAPIView):
	"""This class handles the http GET, PUT and DELETE requests."""
	queryset = User.objects.all()
	serializer_class = UserSerializer

class CreateShoeView(generics.ListCreateAPIView):
	"""
	API endpoint that allows Shoes to be viewed or edited.
	"""
	queryset = Shoe.objects.all()
	serializer_class = ShoeSerializer
	def perform_create(self, serializer):
		"""Save the post data when creating a new bucketlist."""
		serializer.save()

class ShoeDetailsView(generics.RetrieveUpdateDestroyAPIView):
	"""This class handles the http GET, PUT and DELETE requests."""
	queryset = Shoe.objects.all()
	serializer_class = ShoeSerializer

class CreateTransactionsView(generics.ListCreateAPIView):
	"""
	API endpoint that allows Transactions to be viewed or edited.
	"""
	queryset = Transactions.objects.all()
	serializer_class = TransactionsSerializer
	def perform_create(self, serializer):
		"""Save the post data when creating a new bucketlist."""
		serializer.save()

class TransactionsDetailsView(generics.RetrieveUpdateDestroyAPIView):
	"""This class handles the http GET, PUT and DELETE requests."""
	queryset = Transactions.objects.all()
	serializer_class = TransactionsSerializer