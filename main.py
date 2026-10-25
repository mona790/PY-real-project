
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json



# ==========================================
# CREATE FASTAPI APPLICATION
# ==========================================

app = FastAPI()


# ==========================================
# PYDANTIC EMPLOYEE MODEL
# ==========================================

class EmployeeInput(BaseModel):
    name: str
    age: int
    role: str


# ==========================================
# READ EMPLOYEES FROM JSON
# ==========================================

def read_all_employees():

    try:
        with open("employees.json", "r") as json_file:
            employee_records = json.load(json_file)

        return employee_records

    except FileNotFoundError:
        return []


# ==========================================
# SAVE EMPLOYEES TO JSON
# ==========================================

def save_all_employees(records_to_save):

    with open("employees.json", "w") as json_file:
        json.dump(records_to_save, json_file, indent=4)


# ==========================================
# CREATE NEXT EMPLOYEE ID
# ==========================================

def create_next_id(existing_records):

    if len(existing_records) == 0:
        return 1

    largest_id = 0

    for single_record in existing_records:

        current_id = single_record["id"]

        if current_id > largest_id:
            largest_id = current_id

    next_id = largest_id + 1

    return next_id


# ==========================================
# GET - VIEW ALL EMPLOYEES
# ==========================================

@app.get("/employees")
def get_all_employees():

    employee_records = read_all_employees()

    return employee_records


# ==========================================
# GET - SEARCH EMPLOYEE BY ID
# ==========================================

@app.get("/employees/{requested_id}")
def find_employee(requested_id: int):

    employee_records = read_all_employees()

    for single_record in employee_records:

        if single_record["id"] == requested_id:
            return single_record

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )


# ==========================================
# POST - ADD EMPLOYEE
# ==========================================

@app.post("/employees")
def add_employee(new_employee_data: EmployeeInput):

    employee_records = read_all_employees()

    generated_id = create_next_id(employee_records)

    new_employee_record = {
        "id": generated_id,
        "name": new_employee_data.name,
        "age": new_employee_data.age,
        "role": new_employee_data.role
    }

    employee_records.append(new_employee_record)

    save_all_employees(employee_records)

    return {
        "message": "Employee added successfully",
        "employee": new_employee_record
    }


# ==========================================
# PUT - UPDATE EMPLOYEE
# ==========================================

@app.put("/employees/{requested_id}")
def update_employee(
    requested_id: int,
    updated_employee_data: EmployeeInput
):

    employee_records = read_all_employees()

    for single_record in employee_records:

        if single_record["id"] == requested_id:

            single_record["name"] = updated_employee_data.name
            single_record["age"] = updated_employee_data.age
            single_record["role"] = updated_employee_data.role

            save_all_employees(employee_records)

            return {
                "message": "Employee updated successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )


# ==========================================
# DELETE - REMOVE EMPLOYEE
# ==========================================

@app.delete("/employees/{requested_id}")
def delete_employee(requested_id: int):

    employee_records = read_all_employees()

    for single_record in employee_records:

        if single_record["id"] == requested_id:

            employee_records.remove(single_record)

            save_all_employees(employee_records)

            return {
                "message": "Employee deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )
