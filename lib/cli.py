from functions import exit_application, list_all_departments, get_department_by_id, get_department_by_name
def menu():
    print("Select an option: ")
    print("0. Exit application")
    print("1. List all department")
    print("2. Find department by id")
    print("3. Find department by name")        
# def main():
#     while True:
#         menu()
#         choice = input(":")
#         if choice == "0":
#             exit_application()
#         elif choice == "1":
#             list_all_departments()
#         elif choice == "2":
#             get_department_by_id()
#         elif choice == "3":
#             get_department_by_name()
#         else:
#             print("Invalid choice: Try again")
# main()