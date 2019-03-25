from django.test import TestCase

from .models import CustomUser

class CustomUserModelTests(TestCase):

    # Students are defaulted to searching for a partner
    def test_is_searching(self):
        student = CustomUser()
        self.assertTrue(student.is_searching)

    # Student checks that they are not searching
    def test_not_searching(self):
        student = CustomUser()
        student.is_searching = False
        self.assertEqual(student.is_searching, False)

    #Student has no image upon creation
    def test_no_image(self):
        student = CustomUser()
        self.assertEqual("", student.image.__str__())

    #Student uploads a profile picture
    def test_has_image(self):
        student = CustomUser()
        picture = "test_image.jpg"
        student.image = picture
        self.assertEqual(student.image, picture)

    #Student has no description upon creation
    def test_no_description(self):
        student = CustomUser()
        self.assertEqual("", student.description)

    #Student has no availability upon creation
    #def test_no_availability(self):
    #    student = CustomUser()
    #    self.assertEqual("", student.availability)

    #Student has no desired qualities upon creation
    #def test_no_qualities(self):
    #    student = CustomUser()
    #    self.assertEqual("", student.qualities)

    #Student has no profile email upon creation
    #def test_no_profile_email(self):
    #    student = CustomUser()
    #    self.assertEqual("", student.profile_email)

    #Student has no phone number upon creation
    #def test_no_phone_number(self):
    #    student = CustomUser()
    #    self.assertEqual("", student.phone_number)

    #Student inputs a location
    def test_has_location(self):
        student = CustomUser()
        student.location = "Clark"
        self.assertEqual("Clark", student.location)
