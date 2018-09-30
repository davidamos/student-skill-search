from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
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

	def test_model_can_create_an_inventory(self):
		"""Test the bucketlist model can create a bucketlist."""
		old_count = Inventory.objects.count()
		self.inventory.save()
		new_count = Inventory.objects.count()
		self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
	"""Test suite for the api views."""
	def setUp(self):
		"""Define the test client and other test variables."""
		self.client = APIClient()
		self.inventory_data = {'shoeIndex': 555,
								'quantity': 5,
								'owner': 2}
		self.response = self.client.post(
			reverse('create'),
		    self.inventory_data,
			format="json")
	def test_api_can_create_a_inventory(self):
		"""Test the api has bucket creation capability."""
		self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)