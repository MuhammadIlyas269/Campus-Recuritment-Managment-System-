from django.urls import path, include
from .views import(
     Home, SignupView, StudentSignupView,CompanySignupView,
)
from django.conf import settings 
from django.conf.urls.static import static 

#create urls here 

app_name = 'core'
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignupView.as_view(), name='signup'),
    path('accounts/signup/student/', StudentSignupView.as_view(), name='student_signup'),
    path('accounts/signup/company/', CompanySignupView.as_view(), name='company_signup'),


]
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)