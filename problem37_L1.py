def sum_of_list(num_list):
    if len(num_list) == 0:
        return 0
    else:
        lst = num_list
        return lst[0] + sum_of_list(lst[1:])

num_list=[44,23,77,11,89,3]
result = sum_of_list(num_list)
print("Sum of the elements:", result)
