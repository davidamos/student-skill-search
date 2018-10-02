# Create your views here.
# helloworld/views.py

from django.http import HttpResponse
from django.shortcuts import render
from helloworld.models import Shoe, User, Transactions, Inventory
from helloworld.serializers import ShoeSerializer, UserSerializer, TransactionSerializer, InventorySerializer
from rest_framework import generics


def index(request):
	return HttpResponse('Hello, World!')

class CreateInventoryView(generics.ListCreateAPIView):
	"""
	API endpoint that allows users to be viewed or edited.
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