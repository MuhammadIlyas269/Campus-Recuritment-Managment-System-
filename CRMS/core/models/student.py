from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    about_me = models.TextField(blank=False)
    email = models.EmailField(max_length=254)
    