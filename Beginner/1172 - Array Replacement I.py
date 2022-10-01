'''
Read an array X[10]. After, replace every null or negative number of X ​by 1. 
Print all numbers stored in the array X.

Input
The input contains 10 integer numbers. These numbers ​​can be positive or negative.

Output
For each position of the array, print "X [i] = x", where i is the position of the array and x is the number stored in that position.
X[0] = 1
'''

cont=-1
x=[]
for a in range (10):
    y=int(input("valor: "))
    if (y<=0):
        x.append(1)
    else:
        x.append(y)

for b in x:
    cont+=1
    print("x[%.1i] ="%cont,b)