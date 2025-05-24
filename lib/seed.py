from __init__ import CONN, CURSOR
from department import Department

def seed_database():
    Department.drop_table()
    Department.create_table()
    
    # insert data into database
    Department.create("Payroll", "Nairobi")
    Department.create("Engineering", "Nairobi")
    Department.create("IT", "Mombasa")
    Department.create("Marketing", "Kisumu")
    Department.create("Agriculture", "Meru")
    
seed_database()
print("Seeding database")