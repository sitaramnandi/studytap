from django.db import models

# Create your models here.
class student(models.Model):
    stname=models.CharField(max_length=100)
    age=models.IntegerField()
    