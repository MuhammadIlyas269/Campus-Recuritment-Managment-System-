from core.models.job import Job
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.views.generic import (
    CreateView, TemplateView, FormView,
)
from django.views import View
from . forms import (
    StudentSignupForm,CompanySignupForm, CompanyRequestForm, StudentRequestForm,
    JobForm,CompanyProfileForm,CompanyAddressForm, StudentProfileForm, StudentAddressForm,
    SkillForm,
)
from .models import (
    Student, User,Company,CompanyAddress,
)
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth.mixins import LoginRequiredMixin
from django import db




# Create your views here.

def REDIRECT_VIEW(request):
    if request.user.is_student:
        return redirect('core:student_page')
    elif request.user.is_company:
        return redirect('core:company_page')
    elif request.user.is_superuser:
        return redirect('core:modrator_page')


class StudentPage(TemplateView):
    template_name = 'studentPage.html'

class CompanyPage(LoginRequiredMixin,TemplateView):
    login_url = reverse_lazy('core:login')
    template_name = 'companyPage.html'

class ModratorPage(LoginRequiredMixin,TemplateView):
    login_url = reverse_lazy('core:login')
    template_name = 'modratorPage.html'

class Home(TemplateView):
    template_name = 'base.html'


class SignupView(TemplateView):
    template_name = 'registration/signup.html'



# Company Signup Request Form 

class CompanySignupRequestView(FormView):
    form_class = CompanyRequestForm
    template_name = 'companyRequestForm.html'
    success_url = reverse_lazy('core:success')

    def form_valid(self,form):
        self.send_mail(form.cleaned_data)
        return super(CompanySignupRequestView, self).form_valid(form)
    
    def send_mail(self,valid_data):
        context = super().get_context_data()
        context['name']= valid_data['name']
        context['registration_no']= valid_data['registration_no']
        context['contact']= valid_data['contact_no']

        message = render_to_string('companyform_template.txt', context)
        #sending mail to admin    
        email = EmailMessage(
            subject = 'Company Signup Request',
            body = message,
            from_email= 'jokermafia269@gmail.com',
            to = [str(valid_data['email'])],
            bcc= [str(valid_data['email']),],
        )
        email.send()

        

# Student signup request form
class StudentSignupRequestView(FormView):
    form_class = StudentRequestForm
    template_name = 'studentRequestForm.html'
    success_url = reverse_lazy('core:success')
    
    def form_valid(self,form):
        self.send_mail(form.cleaned_data)
        return super(StudentSignupRequestView, self).form_valid(form)

    
    def send_mail(self,valid_data):
        context = super().get_context_data()

        context['name'] = valid_data['name']
        context['stud_id'] = valid_data['stud_id']
        context['card_front'] = valid_data['card_front']
        context['card_back'] = valid_data['card_back']
       
        if valid_data['is_alumni']:
            context['transcript'] = valid_data['transcript']
        else:
            context['card_front'] = valid_data['card_front']
            context['card_back'] = valid_data['card_back']
        
        msg = render_to_string('student_email_form.txt',context)
        
        email = EmailMessage(
                subject='Student Signup Request',
                body = msg,
                from_email = "jokermafia269@gmail.com",
                to = [str(valid_data['email']),],
                bcc = [str(valid_data['email']),],
        )
        
        if valid_data['is_alumni']:
            email.attach(valid_data['transcript'].name,valid_data['transcript'].read(),valid_data['transcript'].content_type) 
        else:
            email.attach(valid_data['card_front'].name, valid_data['card_front'].read(), valid_data['card_front'].content_type) 
            email.attach(valid_data['card_back'].name, valid_data['card_back'].read(), valid_data['card_back'].content_type)

        email.send()
        

class StudentSignupView(CreateView):
    model = User
    form_class = StudentSignupForm
    template_name = "registration/signup_form.html"

    def get_context_data(self,**kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)
    
    def form_valid(self,form):
        user = form.save()
        login(self.request, user)
        return redirect('core:REDIRECT_VIEW')


class CompanySignupView(CreateView):
    model = User
    form_class = CompanySignupForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self,**kwargs):
        kwargs['user_type'] = 'company'
        return super().get_context_data(**kwargs)
    
    def form_valid(self,form):
        user = form.save()
        login(self.request, user)
        return redirect('core:REDIRECT_VIEW')

class CreateJobPostView(LoginRequiredMixin,CreateView):
    login_url = reverse_lazy('core:login')
    model = Job
    form_class=JobForm
    template_name = 'createJob.html'
    
    def form_valid(self,form):
        user = Company.objects.get(user = self.request.user)
        form.instance.company = user
        return super().form_valid(form)



class CompanyProfileView(LoginRequiredMixin,View):
    login_url = reverse_lazy('core:login')

    def get(self, request, ):
        profile_form = CompanyProfileForm()
        address_form = CompanyAddressForm()
        context = {
            'address_form':address_form,
            'profile_form':profile_form,
        }
        return render(request,'companyProfile.html', context)
    

    def post(self, request, ):
        profile_form = CompanyProfileForm(request.POST,)
        address_form = CompanyAddressForm(request.POST)
        
        if address_form.is_valid() and profile_form.is_valid():
            address_cd = address_form.cleaned_data
            company_cd = profile_form.cleaned_data

            address_instance = CompanyAddress(country=address_cd['country'],state=address_cd['state'],city=address_cd['city'],address=address_cd['address'])
            address_instance.save()


            try:
                company_instance = Company(user=request.user,registration_no=company_cd['registration_no'], name=company_cd['name'], 
                about=company_cd['about'],comp_email=company_cd['comp_email'],contact=company_cd['contact'],social_link=company_cd['social_link'],
                website=company_cd['website'],address=address_instance)
                company_instance.save()  
            
            except db.DataError:
                address_instance.delete()
                company_instance.delete()

            return redirect('core:company_page')
        return render(request, 'companyProfile.html',{'profile_form':profile_form, 'address_form':address_form})
    

class StudentProfileView(CreateView):
    template_name = "studentProfile.html"
    success_url = reverse_lazy('core:student_page')
    form_classes = {
        'profile_form': StudentProfileForm,
        'address_form': StudentAddressForm,
        'skill_form': SkillForm,
    }

    def profile_form_valid(self,form):
        pass

    def address_form_valid(self,form):
        pass

    def skill_form_valid(self,form):
        pass

    pass

    
    
            


    
        



