## Rectangle Class ##
class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def change_position(self, x, y):
        self.x = x
        self.y = y 
    def get_position(self):
        return self.x, self.y
    def get_area(self):
        return self.width * self.height


# rect = Rectangle(10, -5, 5, 3)
# pos = rect.get_position()
# print(pos)

# rect.change_position(3, 4)
# pos = rect.get_position()
# print(pos)
# area = rect.get_area()
# print(area)

## Group Class ## 

class Group:
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members
    def add(self, name):
        self.members.append(name)
    def delete(self, name):
        if name in self.members:
            self.members.remove(name)
        else:
            raise Exception('Member not in group.')
    def get_members(self):
        return sorted(self.members)

    def merge(self,instance):
        combined_members = self.members + instance.members 
        new_group = Group("Any Name", combined_members)
        return new_group 

g1 = Group('A-Team', ['Tim', 'Clement'])
g2 = Group('B-Team', ["Antoine"])
g3 = g1.merge(g2)
print(g3.get_members())

# g1 = Group("A-Team", ["Tim", "Joe"])
# g1.add('Sally')
# g1.add('Billy')
# members = g1.get_members()
# print(members)

# g1.delete('Joe')
# members = g1.get_members()
# print(members)

# g1.delete('Joe')

    
