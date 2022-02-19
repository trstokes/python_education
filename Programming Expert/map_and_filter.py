import math

lst1 = [1, 2, 3, 4, 5, 6, 7]
new_lst1 = list(map(lambda x: math.sqrt(x), lst1))
# print(new_lst)

lst2 = [[1, 2, 3], [4, 5, 6], [1, 2, 3,], [3, 4]]

new_lst2 = list(filter(lambda x: sum(x) > 6, lst2))
# print(new_lst2)

lst3 = [[1, 2, 3], [4, 5, 6], [1, 2, 3,], [3, 4]]

new_lst3 = filter(lambda y: y % 2 == 0, map(lambda x: sum(x), lst3))
# print(new_lst3)

lst4 = ["algoexpert", "is", "the", "best"]
x = map(len, lst4)
# print(list(x))

lst = [[2, 3, 4], [4, 5, 6], [1, 1, 1], [0, 0], [-5, -7]]
x = filter(lambda a: abs(sum(a)) > 10, lst)
# print(list(x))

lst11 =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_sqrt_lst = filter(lambda x: x % 2 == 0, map(lambda y: y ** 2, lst11))
new_list = (list(even_sqrt_lst))

for i in new_list: 
    print(i)