from django.db import models
from . import Skill
from . import StudentAddress

class Student(models.Model):
    stud_id = models.CharField(max_length=25, null=True, blank=False)
    name = models.CharField(max_length=50)
    about_me = models.TextField(blank=False)
    email = models.EmailField(max_length=254)
    profile_pic = models.ImageField(upload_to="images/", null=True, blank=False)
    skill = models.ManyToManyField(Skill, blank=True, related_name="student_skills")
    address = models.ForeignKey(StudentAddress, related_name="student", null = True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    