# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

DAYS_OF_WEEK = (
    (0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
    (5, 'Saturday'),
    (6, 'Sunday'),
)

class CustomUser(AbstractUser):
    # add additional fields in here
    is_searching = models.BooleanField(default=True)
    image = models.ImageField(upload_to='profile_image', blank=True)
    courses = models.ManyToManyField('Course', blank=True)
    description = models.CharField(max_length=2000, blank=True)
    availability = models.CharField(max_length=1000, blank=True)
    location = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    profile_email = models.CharField(max_length=100, blank=True)
    home_address = models.CharField(max_length=200, blank=True)
    qualities = models.CharField(max_length=1000, blank=True)
    def __str__(self):
        return self.email

class Course(models.Model):
	course_code = models.CharField(max_length=20, blank=False)
	course_section = models.CharField(max_length=4, blank=False)
	course_is_lecture = models.BooleanField(default=True)
	course_professor = models.CharField(max_length=200, blank=False)
	course_location = models.CharField(max_length=100, blank=False)
	course_days = models.CharField(max_length=1, choices=DAYS_OF_WEEK)
	course_start_time = models.TimeField(blank=False)
	course_end_time = models.TimeField(blank=False)

	def __str__(self):
		return '{} {} {} {} {} {} {} {}'.format(self.course_code, self.course_section, str(self.course_is_lecture), self.course_professor, self.course_location, self.course_days, self.course_start_time.strftime("%H:%M"), self.course_end_time.strftime("%H:%M"))

class Description(models.Model):
    your_description = models.CharField(max_length=500, help_text="Enter a description about yourself.", default = "")
    def __str__(self):
        return self.your_description

class Locations(models.Model):
    input_location = models.CharField(max_length=50)
    def __str__(self):
        return self.input_location
