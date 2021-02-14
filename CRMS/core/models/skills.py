from django.db import models

#create your models here

class Skill(models.Model):
    skill = models.CharField(max_length=100, blank= True, unique=True, null=True)
    