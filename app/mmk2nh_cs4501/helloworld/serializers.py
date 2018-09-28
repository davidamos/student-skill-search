# helloworld/serializers.py
from helloworld.models import Shoe, User, Transactions, Inventory
from rest_framework import serializers

class InventorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Inventory
        fields = ('shoeIndex', 'quantity', 'owner')