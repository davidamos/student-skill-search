from django.http import HttpRequest
from django.test import SimpleTestCase
from django.test import TestCase
from django.urls import reverse
from . import views
# views (uses reverse)
class GeneralViewTest(SimpleTestCase):
	def test_home_page_status_code(self):
		response = self.client.get('/')
		self.assertEquals(response.status_code, 200)

class InventoryViewTests(TestCase):
	def test_view_uses_correct_template(self):
		response = self.client.get(reverse('inventoryHomePage'))
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'inventory.html')

class UserViewTests(TestCase):
	def test_view_uses_correct_template(self):
		response = self.client.get(reverse('userHomePage'))
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'user.html')

class ShoeViewTests(TestCase):
	def test_view_uses_correct_template(self):
		response = self.client.get(reverse('shoeHomePage'))
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'shoe.html')

class TransactionViewTests(TestCase):
	def test_view_uses_correct_template(self):
		response = self.client.get(reverse('transactionHomePage'))
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'transactions.html')