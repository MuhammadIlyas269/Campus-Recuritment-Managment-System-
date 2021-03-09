from django.urls import path, include
from .views import(
     Home, SignupView, StudentSignupView,CompanySignupView,
     StudentPage,CompanyPage,ModratorPage,REDIRECT_VIEW, CompanySignupRequestView,
     StudentSignupRequestView,CreateJobPostView,CompanyProfileView,
)
from django.conf import settings 
from django.conf.urls.static import static 
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

#create urls here 

app_name = 'core'
urlpatterns = [
    path('', Home.as_view(), name='home'),

    # path('accounts/', include('django.contrib.auth.urls')),

   

    ########### Rediret View after Successfull Login #############################
    path('redirect/', REDIRECT_VIEW, name='REDIRECT_VIEW'), 
   
   
    ################ Signup request urls ###############
    path('signup/company/',CompanySignupRequestView.as_view(), name = 'company_signup_request'),
    path('signup/student/',StudentSignupRequestView.as_view(), name = 'student_signup_request'),

    ############ Signup Form ################
    path('accounts/signup/', SignupView.as_view(), name='signup'),
    path('accounts/signup/success/', TemplateView.as_view(template_name='success.html'), name='success'),
    
    path('accounts/signup/student/', StudentSignupView.as_view(), name='student_signup'),
    path('accounts/signup/company/', CompanySignupView.as_view(), name='company_signup'),
    
    
    ########### Student urls #####
    path('accounts/student/me/',StudentPage.as_view(), name='student_page'),

    ####### Comapny urls #####    
    path('accounts/company/me/',CompanyPage.as_view(), name='company_page'),
    path('accounts/company/profile/',CompanyProfileView.as_view(), name='company_profile'),
    path('accounts/company/me/createJob/',CreateJobPostView.as_view(), name='create_job'),

    ####### Admin urls #####
    path('admin/', admin.site.urls, name='admin_page'),
    path('accounts/admin/me/',ModratorPage.as_view(), name='modrator_page'),
    
   




]
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)