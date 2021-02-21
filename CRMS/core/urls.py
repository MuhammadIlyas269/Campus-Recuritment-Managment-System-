from django.urls import path, include
from .views import(
     Home, SignupView, StudentSignupView,CompanySignupView,
     StudentPage,CompanyPage,REDIRECT_VIEW,
)
from django.conf import settings 
from django.conf.urls.static import static 
from django.contrib import admin

#create urls here 

app_name = 'core'
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignupView.as_view(), name='signup'),
    path('accounts/signup/student/', StudentSignupView.as_view(), name='student_signup'),
    path('accounts/signup/company/', CompanySignupView.as_view(), name='company_signup'),
   
    path('redirect/', REDIRECT_VIEW, name='REDIRECT_VIEW'),
    
    path('accounts/student/me/',StudentPage.as_view(), name='student_page'),
    path('accounts/company/me/',CompanyPage.as_view(), name='company_page'),
    path('admin/', admin.site.urls, name='admin_page'),




]
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)