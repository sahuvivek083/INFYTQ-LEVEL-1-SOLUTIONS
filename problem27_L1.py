"""
Given 2 positive integers, write a python function to return True if one of
them is 10 or if their sum is 10, else return False.
Sample Input	Expected Output
10,9	        True
2,8	            True
2,9	            False
"""
def numbers_list(*num):
    if 10 in num or sum(num)==10:
        return True
    else:
        return False
print(numbers_list(10,9))

#or
def check_for_ten(num1, num2):
    if 10 in [num1, num2] or sum([num1, num2]) == 10:
        return True
    else:
        return False

print(check_for_ten(10, 9))
