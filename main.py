# from file_manager.file_manager import FileManager
# from json_manager.json_manager import JsonManager
# from organizations.organizations import Organization
from SQL_repo.sql_repo import (Organization,
                               Employee,
                               Customer,
                               connect_to_db,
                               SQLAlchemyRepo,
                               )

"""Napravite jednostavnu aplikaciju Contact Manager koja vodi evidenciju o podacima Tvrtke (Organization)
, svim Kupcima (Customers) te svim Djelatnicima (Employees).
Aplikaciju napravite tako da svaka komponenta ima svoj Paket sa svim pripadajućim modulima.
Podaci su pohranjeni u tekstualne datoteke. Za rad s datotekama koristite zaseban Paket FileManager.
"""
# tvrtke = []
# tvrtka = Organization("tvrtka prva d.o.o.", 1, "Adresa 1")
# fm = FileManager()
# employees_file = JsonManager("employees.json")
# customers_file = JsonManager("customers.json")
# products_file = JsonManager("products.json")

def print_organization_info(repo, organization):
    print("Organization: ")
    organization.print_org_info()
    print("Employees: ")
    for employee in repo.get_all_employees_in_organization(organization.id):
        employee.print_employee_info()
    print("Customers: ")
    for customer in repo.get_all_customers_in_organization(organization.id):
        customer.print_customer_info()
        
def create_new_organization(repo):
    name = input("Organization name: ")
    oib = int(input("OIB: "))
    organization = repo.get_org_by_oib(oib)
    if not organization:
        address = input("Address: ")
        email = input("Email: ")
        phone = input("Phone: ")
        organization = Organization(
            name=name,
            oib=oib,
            address=address,
            email=email,
            phone=phone
        )
        repo.create_organization(organization)
    else:
        print(f"Organization with OIB {oib} is allready in database")
    organization.print_org_info()
    return organization


def add_employee(repo, organization):
    name = input("Employee Name: ")
    surname = input("Surname: ")
    oib = int(input("OIB: "))
    function = input("Function: ")
    email = input("Email: ")
    phone = input("Phone: ")
    employee = Employee(
        name=name,
        surname=surname,
        oib=oib,
        function=function,
        email=email,
        phone=phone
    )
    employee.organization = organization
    repo.create_employee(employee)
    
    

def pokreni_aplikaciju(db_name):
    session = connect_to_db(db_name)
    repo = SQLAlchemyRepo(session)
    
    organization = create_new_organization(repo)
    print()
    add_employee(repo, organization)
    
    print("All organizations in database: ")
    for organization in repo.get_all_organizations():
        print_organization_info(repo, organization)


if __name__ == "__main__":
    pokreni_aplikaciju("Organizations.sqlite")

# while True:
#     choice = input("Choose one of following options:\n1 - add employee\n2 - add customer\n"
#                    "3 - list employees\n4 - list customers\n5 - exit\n")
#
#     if choice == "1":
#         if not employees_file.check_file():
#             employees_file.create_file()
#         employees_file.write_json(fm.add_employee())
#     elif choice == "2":
#         if not customers_file.check_file():
#             customers_file.create_file()
#         customers_file.write_json(fm.add_customer())
#     elif choice == "3":
#         if len(tvrtka.employees) == 5:
#             print("You have no employee data yet. Press Enter to return to Menu.")
#             enter = input("")
#             continue
#         else:
#             tvrtka.list_employee_data()
#     elif choice == "4":
#         if len(tvrtka.customers) <= 0:
#             print("You have no customer data yet. Press Enter to return to Menu.")
#             enter = input("")
#             continue
#         else:
#             tvrtka.list_customers_data()
#     else:
#         break
