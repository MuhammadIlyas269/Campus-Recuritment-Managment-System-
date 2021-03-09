from django.http import request
from core.models import company, student
from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import (
    User, Student, Company,Job, CompanyAddress,
    StudentAddress, Skill,
)
#create forms here 

class StudentSignupForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User

    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        return user


class CompanySignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self):
        user = super().save(commit=False)
        user.is_company = True
        user.save()
        return user


class CompanyRequestForm(forms.Form):
    name = forms.CharField(max_length=50, label="Full Name")
    registration_no = forms.CharField(label="Registration No")
    email = forms.EmailField(label="Email")
    contact_no = forms.CharField(label="Contact No")


class StudentRequestForm(forms.Form):
    name = forms.CharField(max_length=50,label='Full Name')
    stud_id = forms.CharField(max_length=25, label='Your Registeration Id',)
    is_alumni = forms.BooleanField(label='Are you Alumni',required=False,widget=forms.CheckboxInput(attrs={'id': 'isAlumni'}))
    card_front = forms.ImageField(label='Upload a front side of Id Card',required=False)
    card_back = forms.ImageField(label='Upload a back side of Id Card',required=False)
    email = forms.EmailField(label='Email')
    transcript = forms.ImageField(label='Transcript', help_text='upload Your Final year Transcript',required=False)



class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ['followers','address','user',]

    # def __init__(self,*args,**kwargs):
    #     user = kwargs.pop('user',None)
        
    #     super(CompanyProfileForm, self).__init__(*args,**kwargs)
    #     self.fields["user"].queryset = User.objects.filter(username=user)

class CompanyAddressForm(forms.ModelForm):
    class Meta:
        model = CompanyAddress
        fields = '__all__' 
    
class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude =['company', 'applicants']

    # def __init__(self,*args,**kwargs):
    #     user = kwargs.pop('user') 
    #     super(JobForm, self).__init__(*args,**kwargs)
    #     self.fields["company"].queryset = Company.objects.filter(user = user)

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['skill','address']


class StudentAddressForm(forms.ModelForm):
    class Meta:
        model = StudentAddress
        fields = '__all__'


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'

    







