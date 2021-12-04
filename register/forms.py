from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# Choice for the years
year_choice = [year for year in range(1921, 2022)]

# Choice teacher or student
TeacherorStudent =(
    ("teacher", "Teacher"),
    ("student", "Student"),
)

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    Teacher_or_Student = forms.ChoiceField(choices=TeacherorStudent)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'Teacher_or_Student',
            'username',
            'email',
            'password1', 
            'password2']

class UserprofileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['file']