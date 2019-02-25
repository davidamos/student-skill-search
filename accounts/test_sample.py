from django.test import TestCase

from .models import CustomUser

class CustomerUserTests(TestCase):

    def dummy_test(self):
        x = 1
        y = 1
        self.assertEqual(x,y)
