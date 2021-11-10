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

def personal(request):
	return render(request, 'register/personal.html')

def landing(request):
	return render(request, 'register/landing.html')

def course(request):

	context = {
		'classes' : classes
	}

	return render(request, 'register/course_page.html', context)