# coding: utf-8
x=range(1000)
y=range(1000)
l=[]
for i in x:
    if i < 100:
        for j in y:
            if i==j:
                l.append((i,j))
            else:
                j+=1
                
l
