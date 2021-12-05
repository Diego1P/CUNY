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