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




