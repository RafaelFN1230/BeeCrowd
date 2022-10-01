'''
Read an integer N (2 < N < 1000). Print the multiplication table of N.
1 x N = N      2 x N = 2N        ...       10 x N = 10N  

Input
The input is an integer N (1 < N < 1000).

Output
Print the multiplication table of N., like the following example.
'''

N=int(input())
result=0
for x in range (1,11):
    result=N*x
    print(x,"x",N,"=",result)