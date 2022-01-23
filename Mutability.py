## Question 2
# x = [1, 2, 3, 4]
# y = x

# z = x[:]

# y.append(3)
# z.append(1)

# y = [1, 2]

# print(x)

## Question 3 
# x = (1, 2, 3)
# y = x 

# z = x

# y += (1, 2)
# z += (2, 3)

# print(z)

## Question 4 - Long Question

def replace(lst, target, swap_value):
    for idx in range(len(lst)):
        element = lst[idx]

        if element == target:
            lst[idx] = swap_value
    

lst = ['tim', 'is', 'great', 'is', 'is', 'yes', 'no', 'blue', 'no']
