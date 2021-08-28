"""
This problem is a practice for Debugging covered on Day 3
The code is supposed to replace each value in a list with
twice the preceding value (and the first value with 0)
What's wrong with the code:
An input of [1,2,3] should give [0,2,4]
Debug the code to get the expected output.
"""
def doublePreceding(values):
    for i in range(len(values)):
        if i > 0:
            values[i] = 2 * values[i - 1]

    values[0]= 0
    return values

print("after: ", doublePreceding([1,2,3,4]))