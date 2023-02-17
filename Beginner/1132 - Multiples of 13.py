'''
Write a program that reads two integer numbers X and Y and calculate 
the sum of all number not divisible by 13 between them, including both.

Input
The input file contains 2 integer numbers X and Y without any order.

Output
Print the sum of all numbers between X and Y not divisible by 13, including them if it is the case.

Input Sample	
100
200

Output Sample
13954
'''
a=int(input())
b=int(input())
soma=0
if a==b:
    if a%13 != 0:
        soma+=a
elif a<b:
    while a!=b+1:
        if a%13 != 0:
            soma+=a
        a+=1
elif a>b:
    while b!=a+1:
        if b%13 != 0:
            soma+=b
        b+=1
print(soma)
