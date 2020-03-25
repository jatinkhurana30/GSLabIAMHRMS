from django.contrib import admin
from .models import Employee,Locations,Projects


# Register your models here.
admin.site.register(Employee)
admin.site.register(Locations)
admin.site.register(Projects)