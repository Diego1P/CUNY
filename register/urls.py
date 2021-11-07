from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='Registry Content'),
    path('student-center/', views.scenter, name='Student Center'),
]
#commennnnnnnnt of code