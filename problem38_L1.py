"""
Write a function build_index_grid(rows, columns) that, given a number of
rows and columns, creates a list of lists of that shape that includes the
'row,column' of that location.
For example, after the following code is executed: new_index_grid = build_index_grid(4,3)
new_index_grid would contain:
[['0,0', '0,1', '0,2'],
['1,0', '1,1', '1,2'],
['2,0', '2,1', '2,2'],
['3,0', '3,1', '3,2']]
Note that these are strings.
"""
def build_index_grid(rows, columns):
    result_list=[]
    for outer in range(rows):
        inner_list=[]
        for inner in range(columns):
            string=str(outer)+","+str(inner)
            inner_list.append(string)
            #print(inner_list)
        result_list.append(inner_list)
    return result_list
rows=4
columns=3
result=(build_index_grid(rows,columns))
print("the matrix is",result)
for i in result:
    print(i)
