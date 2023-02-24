'''
Write an algorithm to read a value A and a value N. 
Print the sum of N numbers from A (inclusive). 
While N is negative or ZERO, a new N (only N) must be read. 
All input values are in the same line.

Input
The input contains only integer values, ​​can be positive or negative.

Output
The output contains only an integer value.

Input Sample
3 2

Output Sample
7

Input Sample
3 -1 0 -2 2

Output Sample
7
'''

x=input().split()
a=0
n=0
soma=0
for b in range (len(x)):
    if int(x[b]) >0 and a ==0:
        a=int(x[b])
    elif int(x[b]) >=0 and n ==0:
        n=int(x[b])
for c in range (n):
    soma+=a
    a+=1
print(soma)