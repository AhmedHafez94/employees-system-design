import employeesManager
import utilities

class FrontendManager:
    def __init__(self):
        self.employees_manger = employeesManager.EmployeesManager()

    def print_menu(self):
        print('\nProgram Options:')
        messages = [
            '1) Add a new employee',
            '2) List all employees',
            '3) Delete by age range',
            '4) Update salary given a name',
            '5) End the program'
        ]
        print('\n'.join(messages))
        msg = F'Enter your choice (from 1 to {len(messages)}): '
        return utilities.input_valid_int(msg, 1, len(messages))
        

    def run(self):
        while True:
            choice = self.print_menu()

            if choice == 1:
                self.employees_manger.add_employee()
            elif choice == 2:
                self.employees_manger.list_emplyoees()
            elif choice == 3:
                age_from = utilities.input_valid_int('Enter age from: ')
                age_to = utilities.input_valid_int('Enter age to: ')
                # for simplicity: I assume no input such as 60 30_oop , but valid one: 30_oop 60 (small large)
                self.employees_manger.delete_employees_with_age(age_from, age_to)
            elif choice == 4:
                name = input('Enter name: ')
                salary = utilities.input_valid_int('Enter new salary: ')
                self.employees_manger.update_salary_by_name(name, salary)
            else:
                break

          