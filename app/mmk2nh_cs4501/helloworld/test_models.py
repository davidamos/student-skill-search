from django.test import TestCase
from django.urls import reverse
from helloworld.models import Shoe, User, Transactions, Inventory

# Create your tests here.
class ModelTestCase(TestCase):
	"""This class defines the test suite for the inventory model."""
	def setUp(self):
		"""Define the test client and other test variables."""
		self.shoeIndex = 123
		self.quantity = 3
		self.owner = 1
		self.inventory = Inventory(shoeIndex=self.shoeIndex, quantity=self.quantity, owner=self.owner)
		self.shoe = Shoe(shoeID=1, name='yeezy', typeID=1, brand='Adidas', price=300.0, tradable=1, sellable=1, userID=123456)
		self.user = User(userID=123456, name='Mert', rating=0.9, shoesOwned=3)

	def test_model_can_create_an_inventory(self):
		"""Test the inventory model can create a inventory."""
		old_count = Inventory.objects.count()
		self.inventory.save()
		new_count = Inventory.objects.count()
		self.assertNotEqual(old_count, new_count)

	def test_model_can_create_an_shoe(self):
		"""Test the inventory model can create a inventory."""
		old_count = Shoe.objects.count()
		self.shoe.save()
		new_count = Shoe.objects.count()
		self.assertNotEqual(old_count, new_count)

	def test_model_can_create_an_user(self):
		"""Test the inventory model can create a inventory."""
		old_count = User.objects.count()
		self.user.save()
		new_count = User.objects.count()
		self.assertNotEqual(old_count, new_count)