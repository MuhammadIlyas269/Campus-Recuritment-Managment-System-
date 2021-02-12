from django.db import models

class Student(models.Model):
    stud_id = models.CharField(max_length=25, null=True, blank=False)
    name = models.CharField(max_length=50)
    about_me = models.TextField(blank=False)
    email = models.EmailField(max_length=254)
    profile_pic = models.ImageField(upload_to="images/", null=True, blank=False)
    