"""
Given a list of numbers, write a python function to exchange the first
n/2 elements of a list with the last n/2 elements. The function should
return the new list.n represents the number of elements in the list.
Assume that it will always be even.
Sample Input	Expected Output
[1,2,3,4,5,6,7,8,9,10]	[10,9,8,7,6,1,2,3,4,5]

l1 = [1,2,3,4,5,6,7,8,9,10]
res = l1[:len(l1) / 2]
"""
def new_list(list):
    res=list[-1:len(list)//2-1:-1]+list[0:len(list)//2]
    return res

list=[1,2,3,4,5,6,7,8,9,10]
print(new_list(list))