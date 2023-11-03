from django.db import models

# Create your models here.
class Studentregister(models.Model):
    fullname=models.CharField(max_length=100)
    department=models.CharField(max_length=30)
    native=models.CharField(max_length=100)
    cgpa=models.FloatField(max_length=5.2)