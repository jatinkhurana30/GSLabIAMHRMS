import json
from collections import OrderedDict

import rest_framework

from ..models import Projects,Locations
from ..serializers import LocationSerializer,ProjectSerializer,EmployeeDetailsSerializer


def update_employee_data(employee, json_request):
    updated_column_list = list(json_request.keys())
    for column in updated_column_list:
        if hasattr(employee, column) and (column != "EMPID" and column != "ID"):
            if ['BASELOCATION','CURRENTLOCATION','PROJECTS'].__contains__(column):
                setattr(employee, column+'_id', json_request[column])
                print(getattr(employee, column))
            else:
                setattr(employee, column, json_request[column])

    return employee


def create_employee_id(employee):
    employee_type = employee.EMPTYPE
    primary_key = employee.ID
    if employee_type.lower() == "regular":
        return f"{primary_key}"
    elif employee_type.lower() == "contractor":
        return f"{primary_key}-C"
    elif employee_type.lower() =='intern':
        return f"{primary_key}-I"


def update_projects_and_locations(employeeserializer):
    for employee in employeeserializer.data:
        current_location_serializer = LocationSerializer(Locations.objects.get(pk=employee['CURRENTLOCATION']))
        base_location_serializer = LocationSerializer(Locations.objects.get(pk=employee['BASELOCATION']))
        project_serializer = ProjectSerializer(Projects.objects.get(pk=employee['PROJECTS']))

        employee['PROJECTS'] = project_serializer.data
        employee['BASELOCATION'] = base_location_serializer.data
        employee['CURRENTLOCATION'] = current_location_serializer.data


