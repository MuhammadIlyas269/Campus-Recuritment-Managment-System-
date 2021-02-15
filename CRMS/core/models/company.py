from django.db import models
from . import CompanyAddress

#create models here

class Company(models.Model):
    name = models.CharField(max_length=50, unique=True, null=True)
    about = models.TextField()
    email = models.EmailField(max_length=254)
    contact = models.CharField(max_length=25, null=True)
    social_link = models.URLField(max_length=255, null=True)
    website = models.URLField(max_length=255, null=True)
    address = models.OneToOneField(CompanyAddress, null=True, unique=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    