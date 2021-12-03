from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import SelectDateWidget


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
    Date_Of_birth = forms.DateField(widget=forms.SelectDateWidget(years=sorted(year_choice, reverse=True)))
    Teacher_or_Student = forms.ChoiceField(choices=TeacherorStudent)
    file = forms.FileField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'Date_Of_birth', 'Teacher_or_Student', 'username', 'email', 'file',
                  'password1', 'password2']