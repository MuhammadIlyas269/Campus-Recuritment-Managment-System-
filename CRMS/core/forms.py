from core.models import company, student
from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import User, Student, Company,Job

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

class JobForm(forms.ModelForm):
    
    class Meta:
        model = Job
        exclude =['applicants']

    def __init__(self,*args,**kwargs):
        user = kwargs.pop('user') 
        super(JobForm, self).__init__(*args,**kwargs)
        self.fields["company"].queryset = Company.objects.filter(user = user)

class CompanyProfileForm(forms.ModelForm):
    
    class Meta:
        model = Company
        exclude = ['followers']

    def __init__(self,*args,**kwargs):
        user = kwargs.pop('user')
        super(CompanyProfileForm, self).__init__(*args,**kwargs)
        self.fields["user"].queryset = User.objects.filter(username=user)
    
    







