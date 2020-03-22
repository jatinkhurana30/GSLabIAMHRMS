from os import link

from rest_framework import generics, status, serializers
from rest_framework import mixins
from .serializers import EmployeeSerializer
from .models import Employee
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .business_views.employee_views import update_employee_data, create_employee_id


class EmployeeList(generics.GenericAPIView):

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Will fetch all the employees from the records"""
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Will add the employee to the database"""
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            employee = Employee.objects.get(pk=serializer['ID'].value)
            print(employee.ID)
            # Create a new employee ID based on auto generated id
            try:
                emp_id = create_employee_id(employee)
                employee.EMPID = emp_id
                employee.save()
                serializer = EmployeeSerializer(employee)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except:
                employee.delete()
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RetrieveEmployee(generics.GenericAPIView):

    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    @staticmethod
    def get_employee_from_db(eid):
        try:
            return Employee.objects.get(EMPID=eid.upper())
        except Employee.DoesNotExist:
            return None

    def get(self, request, eid):
        """Will fetch particular employee with it's employee Id"""
        employee = RetrieveEmployee.get_employee_from_db(eid)
        if employee is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, eid):
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
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
