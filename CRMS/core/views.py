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
    JobForm,CompanyProfileForm,CompanyAddressForm,
)
from .models import (
    Student, User,Company,CompanyAddress,
)
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


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

class CompanyPage(TemplateView):
    template_name = 'companyPage.html'

class ModratorPage(TemplateView):
    template_name = 'modratorPage.html'

class Home(TemplateView):
    template_name = 'base.html'


class SignupView(TemplateView):
    template_name = 'registration/signup.html'




class CompanySignupRequestView(View):
    
    def get(self, request):
        form = CompanyRequestForm()
        data = {'form':form}
        return render(request,'requestForm.html',context=data)
    
    def post(self, request):
        form = CompanyRequestForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            registration_no = form.cleaned_data['registration_no']
            to_email = form.cleaned_data['email']
            contact = form.cleaned_data['contact_no']
            
            context = {
                'name':name,
                'registration_no':registration_no,
                'to_email':to_email,
                'contact':contact
            }
            message = render_to_string('companyform_template.txt', context,)
            
            #sending mail to admin
            
            
            email = EmailMessage(
                subject = 'Company Signup Request',
                body = message,
                from_email= 'jokermafia269@gmail.com',
                to = [str(to_email)],
                bcc= [str(to_email),],
            )

            email.send()
            return render(request, 'success.html')
        return render(request, 'requestForm.html',{'form':form})


class StudentSignupRequestView(FormView):
    form_class = StudentRequestForm
    template_name = 'requestForm.html'
    success_url = reverse_lazy('core:success')
    
    def form_valid(self,form):
        self.send_mail(form.cleaned_data)
        return super(StudentSignupRequestView, self).form_valid(form)

    
    def send_mail(self,valid_data):
        context = super().get_context_data()
    
        
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

class CreateJobPostView(CreateView):

    model = Job
    form_class=JobForm
    template_name = 'createJob.html'
    
    def form_valid(self,form):
        user = Company.objects.get(user = self.request.user)
        form.instance.company = user
        return super().form_valid(form)



class CompanyProfileView(View):
    
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
                company = Company(user=request.user,registration_no=company_cd['registration_no'], name=company_cd['name'], 
                about=company_cd['about'],comp_email=company_cd['comp_email'],contact=company_cd['contact'],social_link=company_cd['social_link'],
                website=company_cd['website'],address=address_instance)
                company.save()  
                

            
            except:
                pass

            return redirect('core:company_page')
        return render(request, 'companyProfile.html',{'profile_form':profile_form, 'address_form':address_form})
    
    

    
    
            


    
        



