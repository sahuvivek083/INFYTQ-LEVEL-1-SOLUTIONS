"""
Write a python function that accepts a list of words and returns the
list of integers representing the length of the corresponding words.
Sample Input	Expected Output
[cat, Come] 	[3,4]
"""
def list_words(words):
    for i in words:
        res=[len(words[0]),len(words[1])]
        return res

words=['cat','Come']
print(list_words(words))

#or
def list_of_count(word_list):
    count_list = []
    for word in word_list:
        count_list.append(len(word))
    return count_list

word_list=["cat","come","vivek"]
print(list_of_count(word_list))
