"""
Write a python function which accepts a list of numbers and returns
true if the list contains a 2 next to a 2. Otherwise it should return false.
Sample Input	        Expected Output
[ 1,2,1,2,3,4,5,2,2]	True
[3,2,5,1,2,1,2]         False
"""
def check_list(list_num):
    if "2,2" in (str(list_num)).replace(" ",""):
        return True
    else:
        return False
list_num=[ 1,2,1,2,3,4,5,2,2]
print(check_list(list_num))

