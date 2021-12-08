from django.contrib import admin
from .models import Course, Profile, Teaches, Registered, Comment

admin.site.register(Course)
admin.site.register(Profile)
admin.site.register(Teaches)
admin.site.register(Registered)
admin.site.register(Comment)
