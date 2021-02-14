from django.db import models
from . import Student

#create models here

class Project(models.Model):
    student = models.ForeignKey(Student, related_name='project', on_delete= models.CASCADE)
    title = models.CharField(max_length=25, null=True)
    about = models.TextField(max_length=250, null=True, blank=True)
    certifications = models.ImageField(upload_to = "images/", null=True, blank=True, unique=True)
    period = models.DateField(null=True, blank=False)
    demo = models.URLField(max_length=250, null=True, blank=True, unique=True)
    
    def __str__(self):
        return self.title
    
    