from os import link

from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status, serializers
from .serializers import EmployeeSerializer, LocationSerializer, ProjectSerializer, EmployeeDetailsSerializer
from .models import Employee,Locations,Projects
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .business_views.employee_views import update_employee_data, create_employee_id,update_projects_and_locations


class EmployeeList(generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeDetailsSerializer
    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: EmployeeDetailsSerializer()})
    def get(self, request):
        """Will fetch all the employees from the records"""
        employees = Employee.objects.all()
        employeeserializer = EmployeeSerializer(employees, many=True)
        update_projects_and_locations(employeeserializer)
        return Response(employeeserializer.data,status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=EmployeeSerializer(), responses={201: EmployeeSerializer})
    def post(self, request):
        """Will add the employee to the database"""
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            employee = Employee.objects.get(pk=serializer['ID'].value)
            # Create a new employee ID based on auto generated id
            try:
                emp_id = create_employee_id(employee)
                employee.EMPID = emp_id
                employee.save()
                employeeserializer = EmployeeSerializer(employee)
                return Response(employeeserializer.data, status=status.HTTP_201_CREATED)
            except:
                employee.delete()
                return Response(status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RetrieveEmployee(generics.UpdateAPIView):
    serializer_class = EmployeeSerializer

    # permission_classes = [IsAuthenticated]
    @staticmethod
    def get_employee_from_db(eid):
        try:
            return Employee.objects.get(EMPID=eid.upper())
        except Employee.DoesNotExist:
            return None

    @swagger_auto_schema(responses={200: EmployeeDetailsSerializer()})
    def get(self, request, eid):
        """Will fetch particular employee with it's employee Id"""
        employee = RetrieveEmployee.get_employee_from_db(eid)
        if employee is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        employee_details_serializer = EmployeeDetailsSerializer(employee)
        return Response(employee_details_serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=EmployeeSerializer())
    def patch(self, request, eid):
        """Will update the fields of the employee with particular employee Id
        """
        employee = RetrieveEmployee.get_employee_from_db(eid)

        if employee is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                employee = update_employee_data(employee, request.data)
                employee.save()
                serializer = EmployeeSerializer(employee)
                return Response(status=status.HTTP_202_ACCEPTED)
            except:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
