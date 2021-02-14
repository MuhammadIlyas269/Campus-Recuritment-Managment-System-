from django.db import models
from . import Student

#create models here 

class Qualification(models.Model):
    student = models.ForeignKey(Student, related_name="Qualification", on_delete=models.CASCADE)
    institute_name = models.CharField(max_length=50, null=True, blank=False)
    degree = models.CharField(max_length=50, null=True, blank=False)
    sessions = models.CharField(max_length=50, null=True, blank=False)
    grade = models.CharField(max_length=50, null=True, blank=False)
    
    def __str__(self):
        return self.institute_name