# helloworld/serializers.py
from helloworld.models import Shoe, User, Transactions, Inventory
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'name', 'rating', 'shoesOwned')

class ShoeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Shoe
		fields = ('id', 'name', 'typeID', 'brand', 'price', 'tradable', 'sellable', 'userID')

class TransactionsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Transactions
		fields = ('id', 'transactionDate', 'transactionType', 'sellerID', 'buyerID', 'value')

class InventorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Inventory
		fields = ('id', 'quantity', 'owner')
