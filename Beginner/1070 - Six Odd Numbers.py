'''
Read an integer value X and print the 6 consecutive odd numbers from X, a value per line, including X if it is the case.

Input
The input will be a positive integer value.

Output
The output will be a sequence of six odd numbers.
'''

n=int(input())
for x in range (n,n+12):
    if (x%2!=0):
        print(x)