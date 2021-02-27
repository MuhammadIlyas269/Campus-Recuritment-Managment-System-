from core.models.job import Job
from django.shortcuts import render,redirect,reverse
from django.contrib.auth import login
from django.views.generic import CreateView, TemplateView
from django.views import View
from . forms import (
    StudentSignupForm,CompanySignupForm, CompanyRequestForm, StudentRequestForm,
    JobForm,
)
from .models import (
    Student, User,Company,
)
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


# Create your views here.

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


class StudentSignupRequestView(View):
    
    def get(self, request):
        form = StudentRequestForm()
        data = {'form':form}
        return render(request, 'requestForm.html',context=data)
    
    def post(self, request):
        form = StudentRequestForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            name = cd['name']
            stud_id = cd['stud_id']
            to_email = cd['email']
            card_front =request.FILES['card_front']
            card_back = request.FILES['card_back']
            is_alumni = cd['is_alumni']
            context = {
                'name':name,
                'stud_id':stud_id,
                'is_alumni':is_alumni, 
                'to_email':to_email,
                'card_front':card_front,
                'card_back':card_back,
                
            }

            # if is_alumni:
            #     transcript = request.FILES['transcript']
            #     context['transcript'] =transcript
            
            msg = render_to_string('student_email_form.txt',context)
            email = EmailMessage(
                subject='Student Signup Request',
                body = msg,
                from_email = "jokermafia269@gmail.com",
                to = [str(to_email),],
                bcc = [str(to_email),],
                # attachments= [card_front,card_back,]
            )
            email.attach(card_front.name, card_front.read(), card_front.content_type)
            email.attach(card_back.name, card_back.read(), card_back.content_type)

            email.send()
            return render(request, 'success.html')
        return render(request, 'requestForm.html',{'form':form})




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
    
    def get_form_kwargs(self):
        kwargs = super(CreateJobPostView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        # kwargs['user'] = self.request.user
        return kwargs

    
        



