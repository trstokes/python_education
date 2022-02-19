# func = lambda x, y, z=0: print(x + y + z)
# func(1, 2, 4)

"""This shows the use of a traditional function."""
def sort_func(x):
    return x[1]

lst = [(1, 2), (-2, -4), (3, 4), (0, 0)]
lst.sort(key=sort_func)
# print(lst)

"""This shows the use of the lambda function."""
lst2 = [(1, 2), (-2, -4), (3, 4), (0, 0)]
lst2.sort(key=lambda x: x[1])
# print(lst2)


mul = lambda x: lambda y: x * y

result = mul(2)
# print(result(3)) # prints 6 (2 * 3)


# Lambda Function Practice 

add_values = lambda x, y, z: x + y + z

# print(add_values(2, 3, 4))


max_length = lambda str1, str2: max(len(str1), len(str2))

# print(max_length("tehran", "tim"))

create_set = lambda lst1, lst2: set(lst1).union(lst2)

print(create_set([1, 2, 3, 4], [3, 5, 4, 2]))




