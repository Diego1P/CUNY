from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.landing, name='Landing-Page'),
    path('course/', views.course, name='Course-Page'),
    path('personal/', views.personal, name='Personal-Page'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='register/login.html'), name='login'),
]

