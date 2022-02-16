from curses.ascii import EM


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name 
        self.last_name = last_name 

    def say_hello(self):
        print(f'Hi my name is {self.first_name} {self.last_name}')


class Employee(Person):

    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self.salary = salary 

    def say_hello(self):
        super().say_hello()
        print(f'My salary is {self.salary}')
       
      
class Manager(Employee):
     def __init__(self, first_name, last_name, salary, department):
        super().__init__(first_name, last_name, salary)
        self.department = department 

class Owner(Person):
    def __init__(self, first_name, last_name, net_worth):
        super().__init__(first_name, last_name)
        self.net_worth = net_worth  
        



# o = Owner('Tehran', 'Stokes', '100000000')
# o.say_hello()
# print(type(o))


## Animal Inheritance ## 

class Animal:
    def __init__(self, age, weight, height):
        self.age = age 
        self.weight = weight
        self.height = height
    
class Mammal(Animal):
    def __init__(self, age, weight, height, sex):
        super().__init__(age, weight, height)
        self.sex = sex 

class Reptile(Animal):
    def __init__(self, age, weight, height, legs):
        super().__init__(age, weight, height)
        self.legs = legs 

class Monkey(Mammal):
    fingers = 5 
    def __init__(self, age, weight, height, sex, color):
        super().__init__(age, weight, height, sex)
        self.color = color

class Lizard(Reptile):
    tail = True 
    def __init__(self, age, weight, height, legs, color):
        super().__init__(age, weight, height, legs)
        self.color = color 
    
e = Mammal(15, 150, 154,'Male')
a = Animal(75, 134, 53)
m = Monkey(13, 282, 84, 'Male', 'Brown')
r = Reptile(13, 84, 92, 5)
l = Lizard(1, 12, 32, 4, 'Yellow')