"""
"99 Bottles of Beer" is a traditional song in the United States and Canada.
It is popular to sing this song during long trips, as it has a repetitive
format which is easy to memorize, and takes a long time to sing.
The song's simple lyrics are as follows:
99 bottles of beer on the wall, 99 bottles of beer. Take one down,
pass it around, 98 bottles of beer on the wall.
The same verse is repeated, each time with one fewer bottle. The song is
completed when the singer or singers reach zero.
Write a python function to generate all the words of the song.
"""
def song():
    total_bottles=99
    for bottle in range(total_bottles,0,-1):
        print(str(bottle)+' bottles of beer on the wall,'+str(bottle)+' bottles of beer. Take one down,pass it around,'+str(bottle-1)+' bottles of beer on the wall.')

print(song())