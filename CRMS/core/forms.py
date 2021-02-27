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


class CompanyRequestForm(forms.Form):
    name = forms.CharField(max_length=50, label="Full Name")
    registration_no = forms.CharField(label="Registration No")
    email = forms.EmailField(label="Email")
    contact_no = forms.CharField(label="Contact No")

class StudentRequestForm(forms.Form):
    name = forms.CharField(max_length=50,label='Full Name')
    stud_id = forms.CharField(max_length=25, label='Your Registeration Id',)
    is_alumni = forms.BooleanField(label='Are you Alumni')
    card_front = forms.ImageField(label='Upload a front side of Id Card')
    card_back = forms.ImageField(label='Upload a back side of Id Card')
    email = forms.EmailField(label='Email')

    # def __init__(self,*args,**kwargs):
    #     is_alumni = kwargs.pop('is_alumni',False)
    #     super(StudentRequestForm,self).__init__(*args,**kwargs)
    #     #check if the student is alumni or not
    #     if is_alumni:
    #         self.fields["transcript"] = forms.ImageField(label='Upload transcript')
        
    # def clean(self):
    #     cleaned_data = super().clean()
    #     is_alumni = cleaned_data.get('is_alumni')
    #     if is_alumni == True:
    #         self.fields["transcript"] = forms.ImageField(label='Upload transcript')
        





