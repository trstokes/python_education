# class Person: 
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        

# p1 = Person("Tim", 21)
# p2 = Person("Bill", 41)

# print(p1.name, p1.age)
# print(p2.name, p2.age)

# # Create attribute outside of class 
# p1.new = "random"
# print(p1.new)

# # Change an attribute
# p1.name = 'random'
# print(p1.name)

## CREATING CLASSES ##
## Create "Fruit" Calls with parameteres - name & calories
# class Fruit: 
#     def __init__(self, name, calories):
#         self.name = name 
#         self.calories = calories

# fruit1 = Fruit("Pineapple", 50)
# fruit2 = Fruit("Strawberry", 30)

# print(fruit1.name, fruit1.calories)
# print(fruit2.name, fruit2.calories)

# # Make a new attribute 
# fruit1.color = 'brown'
# print(f"Please enjoy the {fruit1.name}. It is {fruit1.color} and only has {fruit1.calories} calories!")

## int times string 
# class Foo:
#     def __init__(self, name):
#         self.name = name
    
# a = Foo("a")
# b = Foo("b")
# a.name = b.name
# b.name = "c"
# a.x = 2
# b.x = 1
# x = (a.x + b.x) * (a.name + b.name)
# print(x) # prints bcbcbc


## Class Instantiation Practice
# class ContactInformation:
#     def __init__(self, first_name, last_name, email, phone_number):
#         self.first_name = first_name 
#         self.last_name = last_name
#         self.email = email
#         self.phone_number = phone_number
#         self.country = None


# person1 = ContactInformation("Joe", "Dirt", "J.Dirt@gmail.com", "773-454-4543")
# person2 = ContactInformation("Joe", "Blirt", "J.Blirt@gmail.com", "773-939-0303")

# print(person1.last_name)
# print(person2.first_name)

## METHODS ## 
# class Person:
#     def __init__(self, name):
#         self.name = name
#         self.age = None # Creates attribute to be used later
    
#     def say_hello(self): # Method
#         print(f"Hello, {self.name}! You are awesome!")

#     def set_age(self, age): # Setter Method - Creates new attribute
#         self.age = age

#     def get_age(self): # Getter Method - returns value of attrubute
#         return self.age

# p1 = Person("Tehran")
# p2 = Person("Stokes")

# class Counter: # Keeps track of count
#     def __init__(self,):
#         self.count = 0 
#         self.locked = False

#     def toggle_lock(self):
#         self.locked = not self.locked

#     def increment(self):
#         if self.locked:
#             raise Exception("The counter is locked!")
#         self.count += 1

#     def decrement(self):
#         if self.locked:
#             raise Exception("The counter is locked!")
#         self.count -= 1 

#     def print_count(self):
#         print(f"The current count is {self.count}")

# counter = Counter() # instantiate an instance 
# counter.increment() # calls increment method on instance  +1 
# counter.decrement() # - = 
# counter.print_count() # prints 0
# counter.increment()
# counter.increment()
# counter.print_count() # prints 2

## Toggle Lock Function Test  ## 
# counter = Counter()
# counter.increment()
# counter.decrement()
# counter.print_count()

# counter.toggle_lock()
# counter.decrement()











