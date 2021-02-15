from django.db import models
from . import (
    Student,Job,
)

class SaveJobs(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="Student", null=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="Job", null=True)
    
    def __str__(self):
        return self.student.name