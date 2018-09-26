from django.db import models
from django_mysql.models import ListTextField

# Create your models here.
class Shoe(models.Model):
	index = models.IntegerField(default=-1) # index number, uniqueID
	name = models.CharField(max_length=128) # Name of shoe
	typeID = models.IntegerField(default=-1) # shoe type ID
	brand = models.CharField(max_length=128) # Name of brand
	price = models.DecimalField(default=-1.0, decimal_places=2, max_digits=10)
	tradable = models.IntegerField(default=-1) # tradable flag
	sellable = models.IntegerField(default=-1) # sellable flag
	userID = models.IntegerField(default=-1) # userID -> sellers table

class User(models.Model):
	index = models.IntegerField(default=-1) # sellerID in 'Shoes' correspond to index number, uniqueID 
	name = models.CharField(max_length=128) # Name of user
	rating = models.DecimalField(default=-1.0, max_digits=1, decimal_places=1) # rating of user
	shoesOwned = ListTextField(base_field=models.IntegerField())

class Transactions(models.Model):
	transactionID = models.IntegerField(default=-1) # Transaction ID, uniqueID
	pub_date = models.DateTimeField('transaction date') # Date of transaction
	transactionType = models.IntegerField(default=0) # transaction type: sell
	sellerID = models.IntegerField(default=-1) # sellerID
	buyerID = models.IntegerField(default=-1) # buyerID

class Inventory(models.Model):
	shoeIndex = models.IntegerField(default=-1) # index number
	quantity = models.IntegerField(default=-1)


