from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import SelectDateWidget

# Choice for the years
year_choice = [year for year in range(1921, 2022)]


class UserRegisterForm(UserCreationForm):
    firstName = forms.CharField(max_length=100)
    lastName = forms.CharField(max_length=100)
    Date_Of_birth = forms.DateField(widget=forms.SelectDateWidget(years=sorted(year_choice, reverse=True)))
    SSN = forms.CharField(max_length=4,
                          help_text='Last 4 digits of your Social Security')
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['firstName', 'lastName', 'Date_Of_birth', 'SSN', 'username', 'email',
                  'password1', 'password2']
