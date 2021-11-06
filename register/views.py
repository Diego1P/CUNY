from django.shortcuts import render
from django.http import HttpResponse



classes = [

 {
 	'course_name' : 'Software Engineering',
 	'course_id' : 'CSC 32200',
 	'instructor' : 'Jie Wei',
 	'day' : 'TuThu', 
 	'time' : '12:00 - 14:15',
 	'location' : 'online synchronous',
 },

  {
 	'course_name' : 'Organic Chemistry 2',
 	'course_id' : 'CHEM 26300',
 	'instructor' : 'Mark Biscoe',
 	'day' : 'TuThu', 
 	'time' : '10:00 - 11:50',
 	'location' : 'online synchronous',
 }


]

def home(request):
	return render(request, 'register/home.html')

def scenter(request):

	context = {
		'classes' : classes
	}

	return render(request, 'register/scenter.html', context)