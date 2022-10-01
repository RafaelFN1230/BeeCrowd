'''
Read an integer N. Print the square of each one of the even values from 1 to N including N if it is the case.

Input
The input contains an integer N (5 < N < 2000).

Output
Print the square of each one of the even values from 1 to N, as the given example.

Be carefull! Some language automaticly print 1e+006 instead 1000000. 
Please configure your program to print the correct format setting the output precision.
'''

n=int(input())
if (n>5 and n<2000):
    for x in range(1,n+1):
        if (x%2==0):
            result=x**2
            print("%.1i^2 ="%(x),result)