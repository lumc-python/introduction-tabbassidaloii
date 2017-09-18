# coding: utf-8
x=range(10)
x.reverse()
for i in x:
    if i>1:
        print i, "bottles of beer on the wall," , i , " bottles of beer.\nTake one down and pass it around,", i-1 , "bottle of beer on the wall."
    elif i==1:
        print "1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall."
    else:
        print "No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall."
        
