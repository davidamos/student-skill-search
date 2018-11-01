from django.db import models
from decimal import Decimal
# Create your models here.
class Shoe(models.Model):
	shoeID = models.IntegerField(default=-1) # index number, uniqueID
	name = models.CharField(max_length=128) # Name of shoe
	typeID = models.IntegerField(default=-1) # shoe type ID
	brand = models.CharField(max_length=128) # Name of brand
	price = models.DecimalField(default=Decimal('-1.0'), decimal_places=2, max_digits=10)
	tradable = models.IntegerField(default=-1) # tradable flag
	sellable = models.IntegerField(default=-1) # sellable flag
	userID = models.IntegerField(default=-1) # userID -> sellers table
	def __str__(self):
		return str('Index: ' + str(self.shoeID) + '\n' +
				   'Name: ' + str(self.name) + '\n' +
				   'TypeID: ' + str(self.typeID) + '\n' +
				   'Brand: ' + str(self.brand) + '\n' +
				   'Price: ' + str(self.price) + '\n' +
				   'Tradable: ' + str(self.tradable) + '\n' +
				   'Sellable: ' + str(self.sellable) + '\n' +
				   'userID: ' + str(self.userID) + '\n')

class User(models.Model):
	userID = models.IntegerField(default=-1) # sellerID in 'Shoes' correspond to index number, uniqueID
	rating = models.DecimalField(default=Decimal('-1.0'), max_digits=1, decimal_places=1) # rating of user
	shoesOwned = models.IntegerField(default=-1) # number of shoes owned
	firstName = models.CharField(max_length=20, default='')
	lastName = models.CharField(max_length=20, default='')
	username = models.CharField(max_length=30, default='')
	password = models.CharField(max_length=128, default='')
	def __str__(self):
		return str('UserID: ' + str(self.userID) + '\n' +
				   'Name: ' + str(self.name) + '\n' +
				   'Rating: ' + str(self.rating) + '\n' +
				   'ShoesOwned: ' + str(self.shoesOwned) + '\n')

class Transactions(models.Model):
	transactionID = models.IntegerField(default=-1) # Transaction ID, uniqueID
	transactionDate = models.DateTimeField('transaction date', auto_now_add=True) # Date of transaction
	transactionType = models.IntegerField(default=0) # transaction type: sell
	sellerID = models.IntegerField(default=-1) # sellerID
	buyerID = models.IntegerField(default=-1) # buyerID
	value = models.IntegerField(default=-1) # value of the trade or selling 
	def __str__(self):
		return str('TransactionID: ' + str(self.transactionID) + '\n' +
				   'TransactionDate: ' + str(self.transactionDate) + '\n' +
				   'TransactionType: ' + str(self.transactionType) + '\n' +
				   'SellerID: ' + str(self.sellerID) + '\n' +
				   'BuyerID: ' + str(self.buyerID) + '\n' +
				   'Value: ' + str(self.value) + '\n')

class Inventory(models.Model):
	shoeIndex = models.IntegerField(default=-1) # index number of shoe that corresponds to shoe Table
	quantity = models.IntegerField(default=-1)
	owner = models.IntegerField(default=-1) # userID -> sellers table
	def __str__(self):
		return str('ShoeIndex: ' + str(self.shoeIndex) + '\n' +
				   'Quantity: ' + str(self.quantity) + '\n' +
				   'Owner: ' + str(self.owner) + '\n')

class Authenticator(models.Model):
	userID = models.ForeignKey(User, default = -1, on_delete = models.CASCADE)
	authenticator = models.CharField(max_length=255, primary_key=True, unique=True)
	date_created = models.DateTimeField(auto_now_add=True, blank=True)