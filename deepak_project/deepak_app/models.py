from django.db import models
from django.utils import timezone

class RegisterModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)
    password = models.CharField(max_length=100)

class book_details(models.Model):
    Book_Name=models.CharField(max_length=300)
    Author_Name=models.CharField(max_length=200)
    File_Data=models.FileField()
    Status=models.CharField(max_length=200)
    Create_Date=models.DateField(default=timezone.now)
    Update_Date=models.DateField(null=True)
