# Generated by Django 3.2.9 on 2021-12-04 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0012_profile_teacher_or_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Teacher_or_Student',
            field=models.CharField(choices=[('teacher', 'Teacher'), ('student', 'Student')], max_length=7),
        ),
    ]
