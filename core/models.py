from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    stu_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank = True)

    grade = models.IntegerField()
    enrollment_date = models.DateField()
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True) #set once when created
    updated_at = models.DateTimeField(auto_now=True) #updated everytime model is saved

    def __str__(self):
        return f"{self.name} ({self.id})"

    class Meta: #metadata
        verbose_name = 'Student' #human readable name for admin
        verbose_name_plural = 'Students'
        ordering = ['name']