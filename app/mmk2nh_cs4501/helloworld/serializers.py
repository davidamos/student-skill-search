# helloworld/serializers.py
from helloworld.models import Shoe, User, Transactions, Inventory
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('userID', 'name', 'rating', 'shoesOwned')

class ShoeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Shoe
		fields = ('index', 'name', 'typeID', 'brand', 'price', 'tradable', 'sellable', 'userID')

class TransactionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Transactions
		fields = ('transactionID', 'transactionDate', 'transactionType', 'sellerID', 'buyerID', 'value')

class InventorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Inventory
		fields = ('shoeIndex', 'quantity', 'owner')