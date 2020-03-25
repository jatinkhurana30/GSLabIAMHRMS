from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.
data = {
    "FIRSTNAME": "Ajay",
    "MIDDLENAME": "Singh",
    "LASTNAME": "Khurana",
    "EMAIL": "ajay.khurana@gslab.com",
    "GENDER": "Male",
    "DOJ": "2020-03-20",
    "EMPTYPE": "Employee",
    "STATUS": "Active",
    "SEATID": "VT-9090",
    "EXTENSIONNUMBER": 1234,
    "UNIT": "IDM",
    "DEPARTMENT": "Engineering",
    "CAREERTRACK": "",
    "DESIGNATION": "Software Engineer",
    "PROJECTS": "",
    "MANAGER": "",
    "BASELOCATION": "",
    "CURRENTLOCATION": "",
    "DOB": "",
    "MOBILENUMBER": "989909879"
}


class AddRetrieveEmployees(APITestCase):
    url = '/gslab/iam/hrms/employees/'

    def test_registration(self):
        #Testing post request to add employee data to database
        response = self.client.post(AddRetrieveEmployees.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['EMPID'], 'GS-1')

    def test_registration2(self):
        #Testing get request to retrieve all employees from database
        #Mock data
        self.client.post(AddRetrieveEmployees.url, data)

        response = self.client.get(path=AddRetrieveEmployees.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.data

        # Testing if employee ID is getting generated correctly from the code
        self.assertEqual(response_data[0]['EMPID'], 'GS-1')


class RetrieveUpdateSingleEmployee(APITestCase):
    url = '/gslab/iam/hrms/employees/gs-1'

    # Mock data and add it to database
    @classmethod
    def mock_data(cls,self,data):
        self.client.post('/gslab/iam/hrms/employees/', data)

    def test_registration(self):
        # Mock data and add it to database
        RetrieveUpdateSingleEmployee.mock_data(self,data)

        #Perform get test with employee id
        response = self.client.get(path=RetrieveUpdateSingleEmployee.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.data

        #Testing if employee ID is getting generated correctly from the code
        self.assertEqual(response_data['EMPID'], 'GS-1')

    def test_registration2(self):
        # Mock data and add it to database
        RetrieveUpdateSingleEmployee.mock_data(self, data)

        # Perform patch test with employee id
        response = self.client.patch(path=RetrieveUpdateSingleEmployee.url)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)


