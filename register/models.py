from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User

def registraion_period():
	return datetime.now() + timedelta(days=21)

class Course(models.Model):
	course_name = models.CharField(max_length=30, default='-')
	course_id = models.CharField(max_length=6, default='-')
	instructor = models.ForeignKey(User, on_delete=models.CASCADE)
	days = models.CharField(max_length=10, default='-')
	time = models.CharField(max_length=20, default='-')
	location = models.CharField(max_length=20, default='-')
	registraion_window = models.DateTimeField(default=registraion_period)

	def __str__(self):
		return self.course_name


# 	
#	'course_name' : 'Organic Chemistry 2',
#	'course_id' : 'CHEM 26300',
#	'instructor' : 'Mark Biscoe',
# 	'day' : 'TuThu', 
#	'time' : '10:00 - 11:50',
#	'location' : 'online synchronous',
 

