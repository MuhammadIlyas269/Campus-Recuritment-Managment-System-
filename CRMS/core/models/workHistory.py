from django.db import models
from . import Student

#create models here 

class WorkHistory(models.Model):
    student = models.ForeignKey(Student, related_name="studentAddress", on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, null=True, blank=False)
    designation = models.CharField(max_length=50, null=True, blank=False)
    working_period = models.CharField(max_length=50, null=True, blank=False)
    
    def __str__(self):
        return self.company_name
    