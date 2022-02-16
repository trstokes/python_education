## Lesson ## 
class Student:
    def __init__(self, name, grades=[]):
        self.name = name 
        self.grades = grades

    @staticmethod
    def average_from_grades(grades):
        return sum(grades) / len(grades)

s1 = Student('Tehran', [95, 91, 98, 100])
s2 = Student('Stokes', [95, 96, 100, 100])

# average1 = s1.average_from_grades(s1.grades)
# print(average1)

# average2 = s2.average_from_grades(s2.grades)
# print(average2)

## Physics Class ## 

class Physics: 

    @staticmethod
    def calculate_net_force(mass, acceleration):
        if mass <= 0 or acceleration <= 0:
            return 0.0
        
        return mass * acceleration

    @staticmethod
    def calculate_acceleration(mass, net_force):
        if mass <= 0 or net_force <= 0:
            return 0.0

        return net_force / mass 

    @staticmethod
    def calculate_mass(net_force, acceleration):
        if net_force <= 0 or acceleration <= 0:
            return 0.0

        return net_force / acceleration

print(Physics.calculate_net_force(2, 4))
print(Physics.calculate_acceleration(0, 10))
print(Physics.calculate_mass(40, 10))
