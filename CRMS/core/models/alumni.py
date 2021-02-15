from django.db import models
from django.db.models.base import Model
from . import (
    Company, Student, 
)

#create models here

class Alumni(models.Model):
    student = models.OneToOneField(Student, on_delete=models.SET_NULL, null=True, blank=True, related_name="alumni")
    company = models.ForeignKey(Company,on_delete=models.CASCADE, related_name="company_alumni")
    name = models.CharField(max_length=25, null=True,)
    working_from = models.DateField()
    designation = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.name
    