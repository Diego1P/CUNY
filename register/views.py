from django.contrib.auth import models
from django.db.models.fields import files
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserprofileForm, ClassRegisterForm
from .models import Course, Teaches, Registered, Profile, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import urllib

#drop classes on personal page
def personal(request, course_id = None):

    #registration = Registered.objects.get(id=pk)
    #if request.method == 'POST':
    #    registration.delete()
    #    return redirect('Personal-Page')

    enrolled = []
    regobj = []
    for e in Registered.objects.filter(Student = request.user.id):		
        enrolled.append(e.Course)
        regobj.append(e.id)
    zipping = zip(enrolled, regobj)    
    context = {
        'zipping': zipping,
        'len':regobj
    }
    print('Context is llksajfljasdl;fjl;asjdf;lasjdf;ljkasd;flkjasdl;kfj')
    print(context)
    return render(request, 'register/personal.html',context)

def deletepersonal(request, pk):
    obj = get_object_or_404(Registered, pk=pk)
    obj.delete()
    messages.success(request, f'You have dropped for the class successfully!')
    return redirect('Personal-Page')

def landing(request):
    context = {
        'classes': Course.objects.all(),
        'students':Profile.objects.filter(Teacher_or_Student='student'),
    }
    #print(context)
    return render(request, 'register/landing.html', context)

def commnets(request):
    context = {
        'comments': Comment.objects.all()
    }
    return render(request, 'register/comment_list.html', context)

def course(request):
	# will pass the user register form here,(so student can register)
    usr = request.user
    form = ClassRegisterForm()
    if request.method == 'POST':
        form = ClassRegisterForm(request.POST)
        if form.is_valid():
            new_enrollment = Registered.objects.create(
                Student = request.user,
                Course = form.cleaned_data["Course"]
            )
            new_enrollment.save()
            messages.success(request, f'You have registerd for the class successfully!')			
            return redirect('Personal-Page')
        else:
            print("ERROR : Form is invalid")
            print(form.errors)

    #seding courses to the context below...
    data = dict([(str(e.Course), str(e.Instructor)) for e in Teaches.objects.all()])
    context = {
        'classes': Course.objects.all(),
		'teaches': data, 
		'form': form,
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

@login_required
def complain(request):
    return render(request, 'register/complains.html')

class commentListView(ListView):
    model = Comment
    template_name = 'register/comment_list'
    context_object_name = 'comments'
    ordering = ['date_posted']

class commentDetailView(DetailView):
    model = Comment

class commentCreateView(LoginRequiredMixin ,CreateView):
    model = Comment
    fields = ['title', 'comment']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class commentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['title', 'comment']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.user:
            return True
        return False

class commentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    success_url = '/'

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.user:
            return True
        return False