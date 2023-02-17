'''
Write a program that reads two integer numbers X and Y. 
Print all numbers between X and Y which dividing it by 5 the rest is equal to 2 or equal to 3.

Input
The input file contains 2 any positive integers, not necessarily in ascending order.

Output
Print all numbers according to above description, always in ascending order.

Input Sample
10
18

Output Sample
12
13
17
'''

x=int(input())
y=int(input())
resp=[]
if x>y:
    y+=1
    while y!=x:
        if y%5 == 2 or y%5 == 3:
            resp.append(y)
        y+=1
elif x<y:
    x+=1
    while x!=y:
        if x%5 == 2 or x%5 == 3:
            resp.append(x)
        x+=1
elif x==y:
    if y%5 == 2 or y%5 == 3:
        resp.append(y)

resp.sort()
for a in resp:
    print(a)