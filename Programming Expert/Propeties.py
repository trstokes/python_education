class Person:
    def __init__(self, name):
        self.name = name 
        self._salary = 0   # _ denotes a private attribute (Dont change outside of class)
     
    def get_salary(self):
        return round(self._salary)

    
    def set_salary(self, salary):
        if salary < 0:
            raise ValueError('This is invalid!')
        self._salary = salary
    
    
    salary = property(get_salary, set_salary)



# p = Person('Tehran')
# p.salary = 15
# print(p.salary)

class Time:
    def __init__(self, second):
        self._second = second

    @property
    def second(self):
        print('run')
        return self._second

    @second.setter
    def second(self, second):
        if second < 0 or second > 60:
            raise ValueError('Invalid!')
        self._second = second


# t = Time(54)
# t.second = 59
# print(t.second)






