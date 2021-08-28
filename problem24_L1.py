"""
Given two positive integers. Write a python function to return the greatest
common divisor of the given numbers.
Sample Input	Expected Output
14 and 35	    7
800 and 2800	400
"""
def greatest_common_divisor(num1,num2):
    i=1
    while i<=num1//2 and i<=num2//2:
        if num1%i==0 and num2%i==0:
            gcd=i
        i += 1
    return gcd
num1=14
num2=35
print(greatest_common_divisor(num1,num2))

a=14//2 and 35//2
print(a)
