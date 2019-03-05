from django.test import TestCase

from .models import CustomUser

class CustomUserModelTests(TestCase):

    def test_dummy(self):
        """
        ensure tests work
        """
        x = 1
        y = 1
        self.assertEqual(x,y)

    # Students are defaulted to searching for a partner
    def test_is_searching(self):
        student = CustomUser()
        self.assertTrue(student.is_searching)

    # Student checks that they are not searching
    def test_not_searching(self):
        student = CustomUser()
        student.is_searching = False
        self.assertEqual(student.is_searching, False)

