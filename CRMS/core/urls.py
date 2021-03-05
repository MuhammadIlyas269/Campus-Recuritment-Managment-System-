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

#create urls here 

app_name = 'core'
urlpatterns = [
    path('', Home.as_view(), name='home'),

    # path('accounts/', include('django.contrib.auth.urls')),

    ######### Login and Logout #####################
    path('accounts/login/', auth_views.LoginView.as_view(),name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(),name='logout'),

    ########### Rediret View after Successfull Login #############################
    path('redirect/', REDIRECT_VIEW, name='REDIRECT_VIEW'), 
   
   
    ########## Password reset urls ##################
    path('accounts/password-reset/',auth_views.PasswordResetView.as_view(
             template_name='registration/password/password_reset_form.html',
             subject_template_name='registration/password/password_reset_subject.txt',
             email_template_name='registration/password/password_reset_email.html',
             success_url='/core/accounts/password-reset/done/'),name='password_reset'),
   
    path('accounts/password-reset/done/',auth_views.PasswordResetDoneView.as_view(
             template_name='registration/password/password_reset_done.html'),name='password_reset_done'),
   
    path('accounts/password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/password/password_reset_confirm.html',
             success_url='/core/accounts/password-reset-complete/' ),name='password_reset_confirm'),
    
    path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password/password_reset_complete.html' ),name='password_reset_complete'),



    ############ Signup Form ################
    path('accounts/signup/', SignupView.as_view(), name='signup'),
    path('accounts/signup/student/', StudentSignupView.as_view(), name='student_signup'),
    path('accounts/signup/company/', CompanySignupView.as_view(), name='company_signup'),
   
    
    #uers Page + admin panel
    path('accounts/student/me/',StudentPage.as_view(), name='student_page'),
    
    path('accounts/company/me/',CompanyPage.as_view(), name='company_page'),
    path('accounts/company/profile/',CompanyProfileView.as_view(), name='company_profile'),
    path('accounts/company/me/createJob/',CreateJobPostView.as_view(), name='create_job'),

    path('accounts/admin/me/',ModratorPage.as_view(), name='modrator_page'),
    path('admin/', admin.site.urls, name='admin_page'),
    
    #signup request urls
    path('signup/company/',CompanySignupRequestView.as_view(), name = 'company_signup_request'),
    path('signup/student/',StudentSignupRequestView.as_view(), name = 'student_signup_request'),




]
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)