class RunCodeInterface: 
    def compile_code(self):
        raise NotImplementedError('You must implement compile_code()')

    def execute_code(self):
        raise NotImplementedError('You must implement execute_code()')

class GoCode(RunCodeInterface):
    def compile_code(self):
        print('Compile Go code')
    
    def execute_code(self):
        print("Execute Go Code")

class JavaCode(RunCodeInterface):
    def compile_code(self):
        print('Compile Java Code')

    def execute_code(self):
        print('Execute Java Code')


def run_code(code : RunCodeInterface):
    code.compile_code()
    code.execute_code()

# go = GoCode()
# run_code(go)


## Shape Interface ## 

import math 

class ShapeInterface:
    def get_area(self):
        raise NotImplementedError

    def get_perimeter(self):
        raise NotImplementedError

class Square(ShapeInterface):
    def __init__(self, side_length):
        self.side_length = side_length 

    def get_area(self):
        return self.side_length ** 2

    def get_perimeter(self):
        return self.side_length * 4

class Circle(ShapeInterface):
    def __init__(self, radius):
        self.radius = radius 

    def get_area(self):
        return (math.pi * (self.radius ** 2))

    def get_perimeter(self):
        return 2 * math.pi * self.radius


s = Square(3)
print(s.get_area())
print(s.get_perimeter())

c = Circle(5)
print(c.get_perimeter())
print(c.get_area())