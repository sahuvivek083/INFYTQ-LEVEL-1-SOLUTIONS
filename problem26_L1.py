"""
Given a string, write a python function to return True if the strings
"mat" and "jet" appear the same number of times in the given string,
else return False.
Note: Perform case insensitive string comparison wherever necessary.

Sample Input	                    Expected Output
Jet on the Mat but mat is too long	False
mat jet Jet Mat	                    True

string = "mat jet Jet Mat"
"""
def check_occurance(string):
    if string.lower().count("mat")==string.lower().count("jet"):
        return True
    else:
        return False

string1="Jet on the Mat but mat is too long"
print(check_occurance(string1))
string= "mat jet Jet Mat"
print(check_occurance(string))