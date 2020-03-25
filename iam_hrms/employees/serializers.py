from rest_framework import serializers
from .models import Employee, Locations, Projects
from django.db import models


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        # fields = ['FIRSTNAME','LASTNAME']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'


class EmployeeDetailsSerializer(serializers.ModelSerializer):
    CURRENTLOCATION = LocationSerializer()
    BASELOCATION = LocationSerializer()
    PROJECTS = ProjectSerializer()

    class Meta:
        model = Employee
        fields = ['EMPID','FIRSTNAME','MIDDLENAME','LASTNAME','EMAIL','GENDER','DOJ','EMPTYPE','STATUS','CREATIONDATE','LASTUPDATEDDATE',
            'LASTWORKINGDATE','SEATID','EXTENSIONNUMBER','UNIT','DEPARTMENT','CAREERTRACK','DESIGNATION','PROJECTS','MANAGER','CURRENTLOCATION','BASELOCATION','DOB','MOBILENUMBER']
