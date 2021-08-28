"""
Write a python function to find out whether a number is divisible by the
sum of its digits. If so return True,else return False.
Sample Input	Expected Output
42	            True
66	            False
"""
def divisible_by_sum(num):
    total=0
    for digit in str(num):
        total +=int(digit)

    if num % total==0:
        return True
    else:
        return False
num=42
print(divisible_by_sum(num))
