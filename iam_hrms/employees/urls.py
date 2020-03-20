from django.urls import path
from .views import EmployeeList,RetrieveEmployee



urlpatterns = [
    path('employees/', EmployeeList.as_view()),
    path('employees/<str:eid>',RetrieveEmployee.as_view())
]