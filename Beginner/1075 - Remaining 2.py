'''
Read an integer N. Print all numbers between 1 and 10000, which divided by N will give the rest = 2.

Input
The input is an integer N (N < 10000)

Output
Print all numbers between 1 and 10000, which divided by n will give the rest = 2, one per line.
'''

N=int(input())

for x in range (1,10000):
    if (x%N==2):
        print(x)

