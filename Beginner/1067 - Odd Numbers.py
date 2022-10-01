'''
Read an integer value X (1 <= X <= 1000).  
Then print the odd numbers from 1 to X, each one in a line, including X if is the case.

Input
The input will be an integer value.

Output
Print all odd values between 1 and X, including X if is the case.
'''

n=int(input())
for x in range (n+1):
    if (x%2!=0):
        print(x)