from django.db import models


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_id = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

# 	need to finish the Course model, and add the max length attrib to fields
#	'course_name' : 'Organic Chemistry 2',
#	'course_id' : 'CHEM 26300',
#	'instructor' : 'Mark Biscoe',
# 	'day' : 'TuThu', 
#	'time' : '10:00 - 11:50',
#	'location' : 'online synchronous',


