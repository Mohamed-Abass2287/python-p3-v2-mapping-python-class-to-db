from department import Department

def exit_application():
    print("Bye bye")
    exit()
    
def list_all_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)
def get_department_by_id():
    id = input("Enter the department's id: ")
    department = Department.find_by_id(id)
    if department:
        print(department)
    else:
        print(f'Department with id of {id} is not found')
        
def get_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    if department:
        print(department)
    else:
        print(f'Department with name {name} is not found')