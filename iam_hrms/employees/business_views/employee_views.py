import json


def update_employee_data(employee, json_request):
    updated_column_list = list(json_request.keys())
    for column in updated_column_list:
        if hasattr(employee, column):
            setattr(employee, column, json_request[column])
            print(getattr(employee, column))

    return employee


def create_employee_id(employee):
    employee_type = employee.EMPTYPE
    primary_key = employee.ID
    if employee_type.lower() == "employee":
        return f"GS-{primary_key}"
    elif employee_type.lower() == "contractor":
        return f"GSC-{primary_key}"
