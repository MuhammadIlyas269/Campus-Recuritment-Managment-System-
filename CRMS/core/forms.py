from core.models import student
from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import User, Student, Company

#create forms here 

class StudentSignupForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User

    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        Student.objects.create(user=user)
        return user


class CompanySignupForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User

    def save(self):
        user = super().save(commit=False)
        user.is_company = True
        user.save()
        Company.objects.create(user=user)
        return user
