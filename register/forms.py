from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


# Choice teacher or student


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1', 
            'password2']

    def clean(self):
        cleaned_data = super(UserRegisterForm, self).clean()
        email = cleaned_data.get("email")

        check_email = User.objects.filter(email=email)
        if check_email:
            raise forms.ValidationError("A user with the same email is already registered!")
            return cleaned_data


class UserprofileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['file', 'Teacher_or_Student']
