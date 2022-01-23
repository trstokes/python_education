# Lecture example 1: 
# lst = [2, 1, 3, 4, 2, 3, 2, 1]
# lst.sort()
# print(lst)

# Lecture example 2: 
# lst = [2, 1, 3, 4, 2, 3, 2, 1]
# print(sorted(lst))
# print(lst)

# Lecture example 3: 
# lst = [2, 1, 3, 4, 2, 3, 2, 1]
# lst.sort(reverse=True)
# print(lst)

# Lecture example 4:
# lst = [[1, -2], [3, -4], [5, -6], [-1, -2], [0, 0]]
# lst.sort()
# print(lst)

# Lecture example 4:
# def sort_second_index(item):
#     return item[1]

# lst = [[1, -2], [3, -4], [5, -6], [-1, -2], [0, 0]]
# lst.sort(key=sort_second_index)
# print(lst)

# Question 1 - What does the following code output?
# lst = [3, 4, 2, -1, 2]

# print(lst.sort()) # prints None 

# Question 2 - What does the following code output?
# lst = [3, 4, 2, -1, 2]
# lst.sort(reverse=True)
# print(lst) # Returns [4, 3, 2, 2, -1]

# Question 3 - What does the following code output?
# lst = [3, 4, 5, 0.1, 2]

# sorted(lst, reverse=True)
# print(lst) # Returns [[3, 4, 5, 0.1, 2]

# Question 4 - What does the following code output?
# people = {'Tim': 21, 'Joe': 18, 'Sarah': 25, 'Jennie': 26, 'Bill': 34}

# result = sorted(people, key=people.get)
# print(result)