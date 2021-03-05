from django.db import models

#create models here

class CompanyAddress(models.Model):
    country = models.CharField(max_length=25, null=True)
    city = models.CharField(max_length=25, null=True)
    state = models.CharField(max_length=25, null=True)
    address = models.CharField(max_length=100, null=True, unique=True)
    
    def __str__(self):
        return self.address