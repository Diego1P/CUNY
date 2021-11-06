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


def home(request):
    return render(request, 'register/home.html')


def scenter(request):
    context = {
        'classes': classes
    }

    return render(request, 'register/scenter.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register/register.html', {'form': form})
