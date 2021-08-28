"""
Given a list of integers and a number. Write a python function to find and
return the sum of the elements of the list.
Note: Don't add the given number and also the numbers present before and
after the given number in the list .

Sample input	                        Expected output
#num_list=[1,2,3,4], number=2	            4
num_list=[1,2,2,3,5,4,2,2,1,2],number=2	    5
#num_list=[1,7,3,4,1,7,10,5],number=7	    9
#num_list=[1,2,1,2],number=2	            0
"""
def sum_of_elements(num_list, number):
    result_sum = 0
    del_index_list = []
    actual_index_list = []

    for i in range(len(num_list)):
        actual_index_list.append(i)

        if num_list[i] == number:
            if i > 0 and i != len(num_list) - 1:
                del_index_list.append(i - 1)

            del_index_list.append(i)

            if i < len(num_list) - 1:
                del_index_list.append(i + 1)

    print ("actual index: ", actual_index_list)
    print ("del index: ", del_index_list)

    for i in actual_index_list:
        if i not in del_index_list:
            result_sum += num_list[i]

    return result_sum

num_list = [1, 2, 2, 3, 5, 4, 2, 2, 1, 2
number = 2

print(sum_of_elements(num_list, number))

"""
num_list = [1, 2, 3, 4]
number = 2
4

num_list = [1, 2, 2, 3, 5, 4, 2, 2, 1, 2]
number = 2
5

num_list = [1, 7, 3, 4, 1, 7, 10, 5]
number = 7
9

num_list = [1, 2, 1, 2]
number = 2
0
"""
