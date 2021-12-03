from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

classes = [

    {
        'course_name': 'Software Engineering',
        'course_id': 'CSC 32200',
        'instructor': 'Jie Wei',
        'day': 'TuThu',
        'time': '12:00 - 14:15',
        'location': 'online synchronous',
    },

    {
        'course_name': 'Organic Chemistry 2',
        'course_id': 'CHEM 26300',
        'instructor': 'Mark Biscoe',
        'day': 'TuThu',
        'time': '10:00 - 11:50',
        'location': 'online synchronous',
    }


]


def personal(request):
	return render(request, 'register/personal.html')

def landing(request):
	return render(request, 'register/landing.html')

def course(request):

    context = {
        'classes': classes
    }

    return render(request, 'register/course_page.html', context)



def save_file(f):
    with open('register/uploads/'+f.name,'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            save_file(request.FILES['file'])
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register/register.html', {'form': form})

  #return render(request, 'register/course_page.html', context)
  #this was in the main file, may be needed?

