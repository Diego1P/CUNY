from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserprofileForm
from .models import Course, Teaches, Registered, Profile
from django.views import generic
import urllib


def personal(request):
	usr = request.user
	enrolled = []
	for e in Registered.objects.filter(Student = usr.id):		
		enrolled.append(str(e.Course))
	context = {
		'enrolled': enrolled,
	}
	print(context)
	return render(request, 'register/personal.html',context)

def landing(request):
    context = {
        'classes': Course.objects.all(),
        'students':Profile.objects.filter(Teacher_or_Student='student'),
    }
    print(context)
    return render(request, 'register/landing.html', context)

def course(request):
    context = {
        'classes': Course.objects.all()
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