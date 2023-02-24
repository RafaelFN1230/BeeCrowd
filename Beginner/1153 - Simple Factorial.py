'''
Read a value N. Calculate and write its corresponding factorial. 
Factorial of N = N * (N-1) * (N-2) * (N-3) * ... * 1.

Input
The input contains an integer value N (0 < N < 13).

Output
The output contains an integer value corresponding to the factorial of N.

Input Sample	
4

Output Sample
24
'''

def fatorial(t,resp):
    while t>0:
        resp*=t
        return fatorial(t-1,resp)
    print(resp)
        
n=int(input())
fatorial(n,1)
