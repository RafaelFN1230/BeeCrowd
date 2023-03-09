'''
Read an integer N and compute all its divisors.

Input
The input file contains an integer value.

Output
Write all positive divisors of N, one value per line.

Input Sample	
6

Output Sample
1
2
3
6
'''

n=int(input())
x=1
while x!=n+1:
    if n%x==0:
        print(x)
    x+=1