from django.test import TestCase

from .models import CustomUser
from .models import Class

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

    #Student has default image upon creation
    def test_no_image(self):
        student = CustomUser()
        self.assertEqual("default.png", student.image.__str__())

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

    # Student enters a description of "I'm a CS student" for their profile
    def test_description(self):
        student = CustomUser()
        student.description = "I'm a CS student"
        self.assertEqual("I'm a CS student", student.description)

    #Student has no availability upon creation
    def test_no_availability(self):
        student = CustomUser()
        self.assertEqual("", student.availability)

    #Student indicates that they are available on Sundays
    def test_has_availability(self):
        student = CustomUser
        student.availability = "Sunday"
        self.assertEqual("Sunday", student.availability)

    # Student has no profile email upon creation
    def test_no_profile_email(self):
       student = CustomUser()
       self.assertEqual("", student.profile_email)

    # Student indicates their email as "test123@gmail.com"
    # def test_has_profile_email(self):
    #     student = CustomUser
    #     student.email = "test123@gmail.com"
    #     self.assertEqual("test123@gmail.com", student.profile_email)

    # Student has no phone number upon creation
    def test_no_phone_number(self):
       student = CustomUser()
       self.assertEqual("", student.phone_number)

    # Student indicates their phone number is (999)-999-9999
    def test_has_phone_number(self):
       student = CustomUser()
       student.phone_number = "(999)-999-9999"
       self.assertEqual("(999)-999-9999", student.phone_number)

    # Student has no location upon creation
    def test_has_location(self):
       student = CustomUser()
       self.assertEqual("", student.location)

    # Student inputs a location
    def test_has_location(self):
        student = CustomUser()
        student.location = "Runk"
        self.assertEqual("Runk", student.location)

    # Student has no qualities upon creation
    def test_no_qualities(self):
        student = CustomUser()
        self.assertEqual("", student.qualities)

    # Student enters that they are punctual in the qualities field on their profile
    def test_qualities(self):
        student = CustomUser()
        student.qualities = "Punctual"
        self.assertEqual("Punctual", student.qualities)

    # Student has no classes upon creation
    # def test_no_classes(self):
    #     student = CustomUser()
    #     self.assertEqual("", student.courses)

    # Student indicates that they are in CS 3240
    def test_has_class(self):
        student = CustomUser()
        course = Class
        course.course_code = "CS 3240"
        self.assertEqual("CS 3240", course.course_code)
