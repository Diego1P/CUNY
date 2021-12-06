from typing_extensions import Required
from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User


def registraion_period():
	return datetime.now() + timedelta(days=21)

class Course(models.Model):
	course_name = models.CharField(max_length=30, default='-')
	course_id = models.CharField(max_length=6, default='-')
	instructor = models.ManyToManyField(User, through='Teaches')
	days = models.CharField(max_length=10, default='-')
	time = models.CharField(max_length=20, default='-')
	location = models.CharField(max_length=20, default='-')
	rating = models.CharField(max_length=3, default='5')
	status = models.CharField(max_length=20, default='open')
	registraion_window = models.DateTimeField(default=registraion_period)

	def __str__(self):
		return self.course_name

class Profile(models.Model):

	TeacherorStudent =(
    ("teacher", "Teacher"),
    ("student", "Student"),
	)

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	Teacher_or_Student = models.CharField(blank=False, max_length=7, choices=TeacherorStudent)
	file = models.FileField(upload_to='uploads')


	def __str__(self):
		return self.user.username

class Teaches(models.Model):
    Instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Registered(models.Model):
    Student = models.ForeignKey(User, on_delete=models.CASCADE)
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)