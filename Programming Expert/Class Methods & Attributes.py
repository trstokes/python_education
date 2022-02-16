# class Employee:
#     average_age = 0
#     average_salary = 0
#     number_of_employees= 0

#     def __init__(self, name, age, salary):
#         self.name = name 
#         self.age = age 
#         self.salary = salary 
        
#         total_age = Employee.average_age * Employee.number_of_employees
#         total_salary = Employee.average_salary * Employee.number_of_employees

#         Employee.average_age = (total_age + age) / (Employee.number_of_employees +1)
#         Employee.average_salary = (total_salary + salary) / (Employee.number_of_employees + 1)

#         Employee.number_of_employees += 1   
        

# e1 = Employee('Tehran', 30, 150000)
# e2 = Employee('Stokes', 30, 250000)
# print(Employee.number_of_employees)
# print(Employee.average_salary)
# print(Employee.average_age)
        