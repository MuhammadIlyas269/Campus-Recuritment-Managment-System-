from django.db import models

# create model here 
class StudentAddress(models.Model):
    country = models.CharField(max_length=25, null=True)
    city = models.CharField(max_length=25, null=True)
    
    def __str__(self):
        return self.city + self.country