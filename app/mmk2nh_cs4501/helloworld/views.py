from django.shortcuts import render
from helloworld.models import Shoe, User, Transactions, Inventory
from rest_framework import viewsets
from helloworld.serializers import InventorySerializer
from django.http import HttpResponse

# Create your views here.
# views.py

def index(request):
	return HttpResponse('Hello, World!')

class InventoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
