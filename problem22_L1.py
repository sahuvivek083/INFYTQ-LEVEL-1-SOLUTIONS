"""
Write a python function to print the given number of diagonal lines of stars.
Sample input: 5
Expected output:
*
.*
..*
...*
....*
Note: Setting the end parameter of the print function to empty string
prevents the issuing of the new line.Example: print(".",end="") will
maintain the cursor in the same line after displaying "."
"""
def diagonal_stars(num):
    for i in range(1,num):
        print(string.rjust(i,'.'))
string='*'
diagonal_stars(5)
