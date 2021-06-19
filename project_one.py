

class Employee():
    def __init__(self, name, age, salary):
        self.name = name 
        self.age = age 
        self.salary = salary 



class EmployeesManger():
    list_of_employees = [] 

    def add_new_employee(self):
        name = input("enter emplyee name: ")
        age = int(input("enter employee age: "))
        salary = int(input("enter employee salary: ")) 
        new_employee = Employee(name, age, salary)
        self.list_of_employees.append(new_employee) 

    def list_all_employees(self):
        for employee in self.list_of_employees:
            print(f"{employee.name} has {employee.age} years old and salary {employee.salary}") 
    def delete_by_age_range(self):
        length = len(self.list_of_employees) 
        age1 = int(input("Enter age from: "))
        age2 = int(input("Enter age to: "))
        new_employees_list = [] 
        for emp in self.list_of_employees:
            if emp.age >= age1 and emp.age <= age2:
                print(f"Deleting {emp.name}") 
            else:
                new_employees_list.append(emp) 

        if len(new_employees_list) > 0:
            self.list_of_employees = new_employees_list    


    def update_salary_by_name(self):
        changes = 0
        name = input("Enter name: ")
        salary = input("Enter new salary: ") 
        for emp in self.list_of_employees:
            if emp.name == name:
                emp.salary = salary 
                changes += 1 
        if changes == 0:
            print("Error: No Employee with such a name") 



    def terminate(self):
        return  



class FrontEndManager():
    employee_manager = EmployeesManger() 
    def start_programme(self):
        print("Programme options: ")
        print("1) Add new employee")
        print("2) list all employees")
        print("3) Delete By age range")
        print("4) Update salary given a name")
        print("5) End The Programme")

        user_choice = input() 
        options = {"1","2","3","4","5"} 
        if user_choice not in options:
            self.start_programme() 
        elif user_choice == "1":
            self.employee_manager.add_new_employee() 
            self.start_programme()
        elif user_choice == "2":
            self.employee_manager.list_all_employees()
            self.start_programme()
        elif user_choice == "3":
            self.employee_manager.delete_by_age_range() 
            self.start_programme()
        elif user_choice == "4":
            self.employee_manager.update_salary_by_name() 
            self.start_programme()
        else:
            self.employee_manager.terminate()                 


front = FrontEndManager() 
front.start_programme()        