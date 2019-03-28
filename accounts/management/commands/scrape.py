'''
Lou's List
Enrollment/Waitlist data since 1980 for any section of any course/lecture/lab/etc.

SIS
For each class:
Average hours spent outside class
How much people felt they learned
How worthwhile people felt this course was
How well defined the course goals/requirements were
How approachable the instructor was
How effective the teacher waitlist

Data since 1980
4-Digit Semester Code
	1168 -> 1 16 8
			0 - 20th century
			1 - 21st century
			  16 - 2016
			     1 - January Semester
			     2 - Spring Semester
			     6 - Summer Semester
			     8 - Fall Semester
'''

import json, urllib.request, time, re
from bs4 import BeautifulSoup 
from openpyxl import Workbook
from openpyxl.chart import ScatterChart, Reference, Series
from django.core.management.base import BaseCommand, CommandError
from datetime import datetime
from ...models import Class

class Command(BaseCommand):
    def handle(self, *args, **options):
    	engineeringGroups = ['APMA', 'BME', 'CHE', 'CEE', 'CompSci', 'ENGR', 'ECE', 'MSE', 'STS', 'SYS']
    	collegeGroups = ['Anthropology', 'Art', 'Astronomy', 'Biology', 'Chemistry', 'Classics', 'Drama', 'EALC', 'Economics', \
    	'English', 'EnviSci', 'French', 'German', 'History', 'Mathematics', 'MDST', 'MESA', 'Music', 'Philosophy', 'Physics', \
    	'Politics', 'PHS', 'Psychology', 'ReliStu', 'Slavic', 'Sociology', 'SPAN', 'Statistics']

    	print("********* REWRITING CLASS DATABASE *********")
    	Class.objects.all().delete()

    	print("********* SAVING E-SCHOOL COURSES *********")
    	for group in engineeringGroups:
    		course_numbers = getAllCoursesFromGroup('1192', group) #1192 represents 2019 Spring
    		for course in course_numbers:
    			info = getCourseInformation('1192', group, course)
    			if info[4] != 'TBA' and info[5] != 'TBA' and info[6] != 'TBA':
    				print('saving course: ', info)
	    			class_info = Class.objects.create(course_code=info[0], course_section=info[1], \
	    				course_is_lecture=info[2], course_professor=info[3], course_days=info[4], \
	    				course_start_time=info[5], course_end_time=info[6], course_location=info[7])

	    print("********* SAVING COLLEGE COURSES *********")
    	for group in collegeGroups:
    		course_numbers = getAllCoursesFromGroup('1192', group) #1192 represents 2019 Spring
    		for course in course_numbers:
    			info = getCourseInformation('1192', group, course)
    			if info[4] != 'TBA' and info[5] != 'TBA' and info[6] != 'TBA':
    				print('saving course: ',info)
	    			class_info = Class.objects.create(course_code=info[0], course_section=info[1], \
	    				course_is_lecture=info[2], course_professor=info[3], course_days=info[4], \
	    				course_start_time=info[5], course_end_time=info[6], course_location=info[7])
	    			
    	self.stdout.write(self.style.SUCCESS("Finished Scraping Lou's List"))

def getCourseInformation(semester, group, course):
	html = BeautifulSoup(urllib.request.urlopen('http://rabi.phys.virginia.edu/mySIS/CS2/page.php?Semester=' + semester + '&Type=Group&Group=' + group).read(), 'html.parser')
	base_element = html.find(text=course)
	base_row = base_element.find_parent('tr')
	row_elements = base_row.find_all('td')

	course_code = base_row['class'][2]
	course_semester = row_elements[0].text.split()[0] + ' ' + row_elements[0].text.split()[1]
	course_section = row_elements[1].text
	course_is_lecture = 'Lecture' in row_elements[2].text
	course_professor = row_elements[5].text
	
	time_and_days = row_elements[6].text.split()
	if len(time_and_days) == 4:
		course_days = time_and_days[0]
		course_start_time = datetime.strptime(time_and_days[1], '%I:%M%p')
		course_end_time = datetime.strptime(time_and_days[3], '%I:%M%p')
	else:
		course_days = 'TBA'
		course_start_time = 'TBA'
		course_end_time = 'TBA'
	course_location = row_elements[7].text

	return (course_code, course_section, course_is_lecture, course_professor, course_days, course_start_time, course_end_time, course_location)

def getAllCoursesFromGroup(semester, group, filter_empty=True):
	courses = []
	html = BeautifulSoup(urllib.request.urlopen('http://rabi.phys.virginia.edu/mySIS/CS2/page.php?Semester=' + semester + '&Type=Group&Group=' + group + '&Print=').read(), 'html.parser')
	for link in html.find_all(class_='Link'):
		if 'EnrollmentGraph' in link['onclick'] and not ("0 /" in link.text or "1 /" in link.text):
			courses.append(re.search("\d{5}", link['onclick']).group(0))
	return courses

# def main():
	# engineeringGroups = ['APMA','BME','CHE','CEE','CompSci','ENGR','ECE','MSE','MAE','STS','SYS']
	# collegeGroups = ['Anthropology','Art','Astronomy','Biology','Chemistry','Classics','Drama','EALC','Economics',\
	# 	'English','EnviSci','French', 'German','History','Mathematics','MDST','MESA','Music','Philosophy','Physics',\
	# 	'Politics','PHS','Psychology','ReliStu','Slavic','Sociology','SPAN','Statistics']
	# for group in engineeringGroups:
	# 	course_numbers = getAllCoursesFromGroup('1192', group)
	# 	for course in course_numbers:
	# 		print(getCourseInformation('1192', group, course))
# main()