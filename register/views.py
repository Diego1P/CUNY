from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserprofileForm

classes = [

    {
        'course_name': 'Software Engineering',
        'course_id': 'CSC 32200',
        'instructor': 'Jie Wei',
        'day': 'TuThu',
        'time': '12:00 - 14:15',
        'location': 'online synchronous',
        'rating': '4/5',
        'status': 'open',
    },
    {
        'course_name': 'Organic Chemistry 2',
        'course_id': 'CHEM 26300',
        'instructor': 'Mark Biscoe',
        'day': 'TuThu',
        'time': '10:00 - 11:50',
        'location': 'online synchronous',
        'rating' : '2/5',
        'status' : 'closed',
    },
    {
        'course_name': 'History of the United States',
        'course_id': 'HIST 24000',
        'instructor': 'Michael Vulis',
        'day': 'TuThu',
        'time': '02:00 - 03:15',
        'location': 'online synchronous',
        'rating' : '5/5',
        'status' : 'open',
    },
    {
        'course_name': 'Compiler Construction',
        'course_id': 'CSC 42000',
        'instructor': 'Matthew Vaz',
        'day': 'MoWe',
        'time': '11:00 - 12:30',
        'location': 'online synchronous',
        'rating' : '1/5',
        'status' : 'open',

    },
    {
        'course_name': 'Methods of Differential Equations',
        'course_id': 'Math 39100',
        'instructor': 'G. Yassiyevic',
        'day': 'MoWe',
        'time': '11:00 - 12:15',
        'location': 'online synchronous',
        'rating' : '3/5',
        'status' : 'full',
    },
    {
        'course_name': 'Calculus I',
        'course_id': 'Math 20100',
        'instructor': 'K. Ravindran',
        'day': 'Fr',
        'time': '03:00 - 05:30',
        'location': 'online synchronous',
        'rating' : '3/5',
        'status' : 'open',
    },


]

students = [
    {
        'student': 'Donald Maga',
        'student_id':'23647986',
    },
    {
        'student': 'Jeff Bozo',
        'student_id':'23647986',
    },
        {
        'student': 'Elon Cuck',
        'student_id':'23647986',
    },
        {
        'student': 'Notch Minecraft',
        'student_id':'23647986',
    },
    {
        'student': 'Joe Biden',
        'student_id':'23647986',
    },
]

def personal(request):
	return render(request, 'register/personal.html')

def landing(request):
    context = {
        'classes': classes,
        'students':students,
    }
    return render(request, 'register/landing.html', context)

def course(request):

    context = {
        'classes': classes
    }

    return render(request, 'register/course_page.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        profile_form = UserprofileForm(request.POST, request.FILES)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
        profile_form = UserprofileForm()

    return render(request, 'register/register.html', {'form': form, 'profile_form' : profile_form})

  #return render(request, 'register/course_page.html', context)
  #this was in the main file, may be needed?

@login_required
def profile(request):
    return render(request, 'register/profile.html')