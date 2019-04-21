# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import ModelForm

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
    name = models.CharField(max_length=60, blank=True)
    is_searching = models.BooleanField(default=True)
    image = models.ImageField(upload_to='profile_image', blank=True)
    courses = models.ManyToManyField('Class', blank=True)
    description = models.CharField(max_length=2000, blank=True)
    availability = models.CharField(max_length=1000, blank=True)
    location = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    profile_email = models.CharField(max_length=100, blank=True)
    home_address = models.CharField(max_length=200, blank=True)
    qualities = models.CharField(max_length=1000, blank=True)
    def __str__(self):
        return self.email

class Class(models.Model):
	course_code = models.CharField(max_length=20, blank=False)
	course_section = models.CharField(max_length=4, blank=False)
	course_is_lecture = models.BooleanField(default=True)
	course_professor = models.CharField(max_length=200, blank=False)
	course_location = models.CharField(max_length=100, blank=False)
	course_days = models.CharField(max_length=100)
	course_start_time = models.TimeField(blank=False)
	course_end_time = models.TimeField(blank=False)

	def __str__(self):
		return self.course_code
		# return '{} {} {} {} {} {} {} {}'.format(self.course_code, self.course_section, str(self.course_is_lecture), self.course_professor, self.course_location, self.course_days, self.course_start_time.strftime("%H:%M"), self.course_end_time.strftime("%H:%M"))

