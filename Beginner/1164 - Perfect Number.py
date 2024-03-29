'''
In mathematics, a perfect number is an integer for which the sum of all its own positive divisors (excluding itself) is equal to the number itself. For example the number 6 is perfect, because 1+2+3 is equal to 6. Your task is to write a program that read integer numbers and print a message informing if these numbers are perfect or are not perfect.

Input
The input contains several test cases. The first contains the number of test cases N (1 ≤ N ≤ 100). Each one of the following N lines contains an integer X (1 ≤ X ≤ 108), that can be or not a perfect number.

Output
For each test case print the message “X eh perfeito” (X is perfect) or “X nao eh perfeito” (X isn't perfect) according with to above specification.

Input Sample	
3
6
5
28

Output Sample
6 eh perfeito
5 nao eh perfeito
28 eh perfeito
'''

n=int(input())

for a in range(n):
    x=int(input())
    soma=0
    divisor=1

    while divisor<x:
        if x%divisor==0:
            soma+=divisor
        divisor+=1
    if soma==x:
        print("%i eh perfeito" %x)
    else:
        print("%i nao eh perfeito" %x)