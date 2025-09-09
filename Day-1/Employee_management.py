employees = []  # list

# Adding employee records
employee = ('BANU', 23, 2333, True)
employees.append(employee)

employee = ('Manu', 23, 3333, True)
employees.append(employee)

employee = ('Ranu', 23, 4333, True)
employees.append(employee)

employee = ('Shanu', 23, 5333, True)
employees.append(employee)

print("Initial employees:")
print(employees)

# Searching for an employee by name
search = 'Manu'  # name to search
index = -1  # default value if not found
i = 0

for emp in employees:
    if emp[0] == search:
        index = i
        break
    i += 1

if index == -1:
    print('Employee not found')
else:
    # Get the found employee
    search_employee = employees[index]
    print("Found employee:", search_employee)

    # Update salary
    salary = float(input('Enter new salary: '))
    # Create new employee tuple with updated salary
    updated_employee = (search_employee[0], search_employee[1], salary, search_employee[3])
    employees[index] = updated_employee
    print("Updated employee:", updated_employee)

# Add a new employee
new_employee = ('Dravid', 50, 200, True)
employees.append(new_employee)
print('After adding Dravid:', employees)

# Delete last employee
employees.pop()
print('After deleting Dravid:', employees)

