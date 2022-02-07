def sort_employees(employees, sort_by):
    sort_indices = ['name', 'age', 'salary']
    sort_index = sort_indices.index(sort_by)

    sorted_employees = []
    employees_copy = employees[:]

    while len(employees_copy) > 0:
        smallest_employee_index = 0

        for i, employee in enumerate(employees_copy):
            current_smallest_value = employees_copy[smallest_employee_index][sort_index]
            if employee[sort_index] < current_smallest_value:
                smallest_employee_index = i


        next_sorted_employee = employees_copy[smallest_employee_index]
        sorted_employees.append(next_sorted_employee)
        employees_copy.pop(smallest_employee_index)

    return sorted_employees

test = sort_employees([['John', 33, 65000], ['Tehran', 31, 350000], ['Stokes', 20, 150000], ['Draco', 18, 100000]], "age")
print(test)