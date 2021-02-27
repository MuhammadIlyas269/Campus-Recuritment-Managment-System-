from django.db import models
from django.shortcuts import reverse
from . import (
    Company, Student,
)

#create models here

class Job(models.Model):
    
    MALE = "m"
    FEMALE = "f"
    NO_PREFERENCE = 'np'
    GENDER_PREFERENCE_CHOICES = [
        (MALE,"Male"),
        (FEMALE,"Female"),
        (NO_PREFERENCE,"No preference"),
        
    ]
    
    PERMANENT = "p"
    PART_TIME = "p_t"
    INTERNSHIP = "Intern"
    CONTRACT_BASE = "Contact"
    EMPLOYMENT_TYPE_CHOICES = [
        (PERMANENT,"Permanent"),
        (PART_TIME,"PartTime"),
        (INTERNSHIP,"Internship"),
        (CONTRACT_BASE,"ContractBase"),
    ]
    
    
    company = models.ForeignKey(Company, related_name="jobs", on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    industry = models.CharField(max_length=100, null=True)
    eligibility_criteria  = models.TextField(null=True)
    created = models.DateField(auto_now_add=True)
    expiry = models.DateField()
    flyer = models.ImageField(upload_to="images/jobs/", null=True, blank=True)
    gender_preference = models.CharField(max_length=2, choices=GENDER_PREFERENCE_CHOICES, default=NO_PREFERENCE,)
    employment_type = models.CharField(max_length=25, choices=EMPLOYMENT_TYPE_CHOICES,)
    status = models.BooleanField(default=True, help_text="show the job recuritment Status")
    applicants = models.ManyToManyField(to=Student, related_name="Applicants" , blank=True,)
    
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('core:company_page')
    