from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.views.generic import CreateView, TemplateView
from . forms import (
    StudentSignupForm,CompanySignupForm,
)
from .models import (
    Student, User,Company,
)

# Create your views here.

def REDIRECT_VIEW(request):
    if request.user.is_student:
        return redirect('core:student_page')
    elif request.user.is_company:
        return redirect('core:company_page')
    elif request.user.is_superuser:
        return redirect('http://127.0.0.1:8000/admin/')


class StudentPage(TemplateView):
    template_name = 'studentPage.html'

class CompanyPage(TemplateView):
    template_name = 'companyPage.html'

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
        return redirect('core:home')


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
        return redirect('core:home')




