# define flatten() below...
def flatten(my_list):
  result = []
  for item in my_list:
    if isinstance(item, list):
      print('List Found!')
      flat_list = flatten(item)
      result += flat_list 
    else:
      result.append(item)
      
  return result


### reserve for testing...
planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]


# print(flatten(planets))

# define the fibonacci() function below...
def fibonacci(n):
  if n == 1:
    return n
  
  if n == 0:
    return n
  
  # recursive step
  print('Recursive call with {0} as input'.format(n))
  return fibonacci(n - 1) + fibonacci(n - 2)


# fibonacci(5)

# Define build_bst() below...
def build_bst(my_list):
  if len(my_list) == 0:
    return "No Child"
  
  middle_idx = len(my_list) // 2
  middle_value = my_list[middle_idx]

  print("Middle index: {0}".format(middle_idx))
  print("Middle value: {0}".format(middle_value))

  tree_node = {"data": middle_value}
  tree_node["left_child"] = build_bst(my_list[ : middle_idx]) # beginning to middle index
  tree_node["right_child"] = build_bst(my_list[middle_idx + 1: ]) # middle index to end

  return tree_node

# For testing
sorted_list = [12, 13, 14, 15, 16]
binary_search_tree = build_bst(sorted_list)
print(binary_search_tree)

# fill in the runtime as a string
# 1, logN, N, N*logN, N^2, 2^N, N!
runtime = "N*logN"

