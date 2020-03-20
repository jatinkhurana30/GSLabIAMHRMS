from django.db import models


# Create your models here.

class Employee(models.Model):
    ID = models.AutoField(auto_created=True, serialize=False, primary_key=True)
    EMPID = models.CharField(unique=True, max_length=100, verbose_name='Employee ID',blank=True, null=True)
    FIRSTNAME = models.CharField(max_length=100, verbose_name='First Name')
    MIDDLENAME = models.CharField(max_length=100, blank=True, null=True)
    LASTNAME = models.CharField(max_length=100)
    EMAIL = models.EmailField(max_length=50, unique=True)
    GENDER = models.CharField(max_length=20)
    DOJ = models.DateField()
    EMPTYPE = models.CharField(max_length=100)
    STATUS = models.CharField(max_length=100)
    SEATID = models.CharField(max_length=100, blank=True, null=True)
    EXTENSIONNUMBER = models.IntegerField(blank=True, null=True)
    UNIT = models.CharField(max_length=100, blank=True, null=True)
    DEPARTMENT = models.CharField(max_length=100, blank=True, null=True)
    CAREERTRACK = models.CharField(max_length=100, blank=True, null=True)
    DESIGNATION = models.CharField(max_length=100)
    PROJECTS = models.CharField(max_length=100, blank=True, null=True)
    MANAGER = models.CharField(max_length=100, blank=True, null=True)
    BASELOCATION = models.CharField(max_length=200, blank=True, null=True)
    CURRENTLOCATION = models.CharField(max_length=200, blank=True, null=True)
    DOB = models.DateField(blank=True, null=True)
    MOBILENUMBER = models.CharField(max_length=100)
