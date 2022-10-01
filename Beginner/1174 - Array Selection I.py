'''
In this problem, your task is to read an array A[100]. 
At the end, print all array positions that store a number less or equal 
to 10 and the number stored in that position.

Input
The input contains 100 numbers. Each number can be integer, floating-point number, positive or negative.

Output
For each number of the array that is equal to 10 or less, print "A [i] = x", 
where i is the position of the array and x is the number stored in the position, 
with one digit after the decimal point.
'''

A=[]
cont=0

for x in range (100):
    a=float(input())
    A.append(a)

for y in A:
    if y<=10:
        print("A[%d] ="%cont,y)
    cont+=1