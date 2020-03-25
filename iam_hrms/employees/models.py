from django.db import models


# Create your models here.

class Projects(models.Model):
    ID = models.AutoField(auto_created=True,primary_key=True)
    NAME = models.CharField(max_length=50)
    DESCRIPTION = models.CharField(max_length=200)

class Locations(models.Model):
    ID = models.AutoField(auto_created=True,primary_key=True)
    ADDRESS = models.CharField(max_length=200)
    COUNTRY = models.CharField(max_length=100)
    STATE = models.CharField(max_length=100)
    CITY = models.CharField(max_length=100)
    PIN = models.IntegerField()

class Employee(models.Model):
    ID = models.AutoField(auto_created=True, serialize=False, primary_key=True)
    EMPID = models.CharField(unique=True, max_length=100, verbose_name='Employee ID',blank=True, null=True, editable=False)
    FIRSTNAME = models.CharField(max_length=100, verbose_name='First Name')
    MIDDLENAME = models.CharField(max_length=100, blank=True, null=True)
    LASTNAME = models.CharField(max_length=100)
    EMAIL = models.EmailField(max_length=50, unique=True)
    GENDER = models.CharField(max_length=20)
    DOJ = models.DateField()
    EMPTYPE = models.CharField(max_length=100)
    STATUS = models.CharField(max_length=100)
    CREATIONDATE = models.DateTimeField(auto_now_add=True)
    LASTUPDATEDDATE = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    LASTWORKINGDATE = models.DateField(blank=True,null=True)
    SEATID = models.CharField(max_length=100, blank=True, null=True)
    EXTENSIONNUMBER = models.IntegerField(blank=True, null=True)
    UNIT = models.CharField(max_length=100, blank=True, null=True)
    DEPARTMENT = models.CharField(max_length=100, blank=True, null=True)
    CAREERTRACK = models.CharField(max_length=100, blank=True, null=True)
    DESIGNATION = models.CharField(max_length=100)
    PROJECTS = models.ForeignKey(Projects,default=1,on_delete=models.SET_DEFAULT)
    MANAGER = models.CharField(max_length=100, blank=True, null=True)
    BASELOCATION = models.ForeignKey(Locations,default=1,on_delete=models.SET_DEFAULT,related_name='base_location')
    CURRENTLOCATION = models.ForeignKey(Locations,default=1,on_delete=models.SET_DEFAULT,related_name='current_location')
    DOB = models.DateField(blank=True, null=True)
    MOBILENUMBER = models.CharField(max_length=100)