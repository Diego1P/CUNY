from django.contrib import admin
from .models import Course, Profile, Teaches, Registered

admin.site.register(Course)
admin.site.register(Profile)
admin.site.register(Teaches)
admin.site.register(Registered)