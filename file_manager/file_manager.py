from organizations.organizations import Organization
from customers.customers import Customer
from employees.employees import Employee


class FileManager:
    customer_id_num = 0
    employee_id_num = 0
    product_id_num = 0

    @classmethod
    def add_customer(cls):
        print("Enter customer information.")
        name = input("Name: ")
        surname = input("Surname: ")
        oib = int(input("OIB: "))
        email = input("Email: ")
        phone = input("Phone: ")
        customer = Customer(name, surname, oib, email, phone)
        print("Press Enter to return to Menu.")
        enter = input("")
        cls.customer_id_num += 1
        return {cls.customer_id_num: {"Name": customer.name,
                                      "Surname": customer.surname,
                                      "OIB": customer.oib,
                                      "Email": customer.email,
                                      "Phone": customer.phone
                                      }
                }

    @classmethod
    def add_employee(cls):
        print("Enter employee information.")
        name = input("Name: ")
        surname = input("Surname: ")
        oib = int(input("OIB: "))
        function = input("Function: ")
        email = input("Email: ")
        phone = input("Phone: ")
        employee = Employee(name, surname, oib, function, email, phone)
        print("Press Enter to return to Menu.")
        enter = input("")
        cls.employee_id_num += 1
        return {cls.employee_id_num: {"Name": employee.name,
                                      "Surname": employee.surname,
                                      "OIB": employee.oib,
                                      "Function": employee.function,
                                      "Address": employee.email,
                                      "Phone": employee.phone
                                      }
                }


  