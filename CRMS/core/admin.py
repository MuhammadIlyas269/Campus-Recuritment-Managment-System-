from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    User,Student,StudentAddress, WorkHistory,
    Qualification, Project, Skill,Company,
    CompanyAddress,Job, Alumni,SaveJobs,
)

# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Student)
admin.site.register(StudentAddress)
admin.site.register(WorkHistory)
admin.site.register(Qualification)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(CompanyAddress)
admin.site.register(Company)
admin.site.register(Job)
admin.site.register(Alumni)
admin.site.register(SaveJobs)