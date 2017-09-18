# coding: utf-8
def f(x):
    return x**2
DicSqu={}
for i in range(100):
    if f(i) < 100:
        DicSqu[i]=f(i)
        
DicSqu
for i in range(len(DicSqu)):
    print DicSqu[i], 'is the square of', i
    
