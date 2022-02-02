class Page: ## Addition Operation 
    def __init__(self, words, page_number):
        self.words = words 
        self.page_number = page_number

    def __str__(self):
        return self.words


        

    def __add__(self, other):
        new_words = self.words + other.words 
        new_page_number = max(self.page_number, other.page_number) + 1
        return Page(new_words, new_page_number)

page1 = Page('Tehran is the best! ', 1)
page2 = Page(' Tehran is going to be rich. ', 2)

# page3 = page1 + page2
# print(page3.words, page3.page_number)

class StoreItem:
    tax = 0.13

    def __init__(self, name, price):
        self.name = name 
        self. price = price 
        self.after_tax_price = 0 
        self.set_after_tax_price()
    
    def set_after_tax_price(self):
        self.after_tax_price = round(self.price * (1 + self.tax), 2)

    def __sub__(self, discount):
        return StoreItem(self.name, self.price - discount)

    def __mul__(self, value):
        return StoreItem(self.name, self.price * value)



# car = StoreItem('Aston Martin', 317000)
# discounted_car = car * 0.8

# print(discounted_car.after_tax_price)


class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    
    def __truediv__(self, factor):
        new_point1 = (self.point1[0] / factor, self.point1[1] / factor)
        new_point2 = (self.point2[0] / factor, self.point2[1] / factor)
        return Line(new_point1, new_point2)

# line1 = Line((10, 5), (20, 10))
# line2 = line1 / 2
# print(line2.point1, line2.point2)

class Book:
    def __init__(self, title, author, pages, id_number):
        self.title = title 
        self.author = author
        self.pages = pages 
        self.id_number = id_number

    def __str__(self):
        output = f'Book({self.title}, {self.author}, {self.id_number})'

        for page in self.pages:
            output += "\n" + str(page)
        
        return output 


    def __len__(self):
        return len(self.pages)


page1 = Page('Page 1!', 1)
page2 = Page('This is page 2.', 2)
book = Book('Tehran is Great', 'Tehran', [page1, page2], 1)
print(book)

 ## Vector Class ## 

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __eq__(self, vector):
        return self.a == vector.a and self.b == vector.b

    def __repr__(self):
        return f"Vector({self.a}, {self.b})"

    def __add__(self, vector):
        new_a = self.a + vector.a
        new_b = self.b + vector.b
        return Vector(new_a, new_b)

    def __sub__(self, vector):
        new_a = self.a - vector.a
        new_b = self.b - vector.b
        return Vector(new_a, new_b)

    def __mul__(self, vector):
        return self.a * vector.a + self.b * vector.b
