""" Module Filen """
import repo_sql_dict as repo
def create_view():
    """Create a new employee record from user input."""
    emp_id = int(input('ID: '))
    name = input('Name: ')
    age = int(input('Age: '))
    salary = float(input('Salary: '))
    is_active = input('Active (y/n): ').strip().lower().startswith('y')

    employee = {'id': emp_id, 'name': name, 'age': age,
                'salary': salary, 'is_active': is_active}

    try:
        repo.create_employee(employee)
        print('Employee Created Successfully.')
    except repo.EmployeeAlreadyExist as ex:
        print(f'Duplicated Employee ID: {ex}')
    except repo.DatabaseError as ex:
        print(f'Database Error in creating employee: {ex}')


def list_employees():
    """List all employees."""
    print('List of Employees:')
    employees = repo.read_all_employee()
    if not employees:
        print("No employees found.")
    else:
        for employee in employees:
            print(employee)


def read_employee_by_id():
    """Read and display employee details by ID."""
    try:
        emp_id = int(input('ID: '))
        employee = repo.read_by_id(emp_id)
        if employee is None:
            print('Employee not found.')
        else:
            print(employee)
    except ValueError:
        print("Invalid ID input.")


def update_employee():
    """Update employee's salary by ID."""
    try:
        emp_id = int(input('ID: '))
        employee = repo.read_by_id(emp_id)
        if employee is None:
            print('Employee Not Found')
        else:
            print(employee)
            salary = float(input('New Salary: '))
            new_employee = {
                'id': employee['id'],
                'name': employee['name'],
                'age': employee['age'],
                'salary': salary,
                'is_active': employee['is_active']
            }
            repo.update(emp_id, new_employee)
            print('Employee updated successfully.')
    except ValueError:
        print("Invalid input.")


def delete_employee():
    """Delete employee by ID."""
    try:
        emp_id = int(input('ID: '))
        employee = repo.read_by_id(emp_id)
        if employee is None:
            print('Employee Not Found')
        else:
            repo.delete_employee(emp_id)
            print('Employee Deleted Successfully.')
    except ValueError:
        print("Invalid input.")


def menu():
    """
    Display menu options and route to appropriate functions.

    Returns:
        int: The chosen menu option.
    """
    message = '''
Options are:
1 - Create Employee
2 - List All Employees
3 - Read Employee By Id
4 - Update Employee
5 - Delete Employee
6 - Exit 
Your Option: '''

    try:
        choice = int(input(message))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 6.")
        return None

    if choice == 1:
        create_view()
    elif choice == 2:
        list_employees()
    elif choice == 3:
        read_employee_by_id()
    elif choice == 4:
        update_employee()
    elif choice == 5:
        delete_employee()
    elif choice == 6:
        print('Thank you for using the Application.')
    else:
        print("Please select a valid option (1-6).")

    return choice


def menus():
    """Run the menu loop until user chooses to exit."""
    choice = None
    while choice != 6:
        choice = menu()


if __name__ == "__main__":
    menus()
