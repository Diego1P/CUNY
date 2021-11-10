from django.urls import path
from . import views 

urlpatterns = [
    path('', views.landing, name='Landing-Page'),
    path('course/', views.course, name='Course-Page'),
    path('personal/', views.personal, name='Personal-Page'),
]
