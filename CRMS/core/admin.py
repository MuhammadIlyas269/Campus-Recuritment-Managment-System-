
# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    User,Student,StudentAddress,
)

admin.site.register(User, UserAdmin)
admin.site.register(Student)
admin.site.register(StudentAddress)