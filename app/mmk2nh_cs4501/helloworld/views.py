# Create your views here.
# helloworld/views.py

from django.http import HttpResponse
from django.shortcuts import render
from helloworld.models import Shoe, User, Transactions, Inventory
from helloworld.serializers import InventorySerializer
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

    