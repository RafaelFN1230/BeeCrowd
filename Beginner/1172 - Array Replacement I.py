'''
Read an array X[10]. After, replace every null or negative number of X ​by 1. 
Print all numbers stored in the array X.

Input
The input contains 10 integer numbers. These numbers ​​can be positive or negative.

Output
For each position of the array, print "X [i] = x", where i is the position of the array and x is the number stored in that position.
X[0] = 1
'''

cont=0
x=[]

for a in range(10):
    X=int(input())
    x.append(X)

for b in x:
    if (b<=0):
        x[cont]=1
    print("X[%i] ="%cont,x[cont])
    cont+=1