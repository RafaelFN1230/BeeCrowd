'''
Write a program that reads a number and print the Fibonacci number corresponding to this read number. 
Remember that the first elements of the Fibonacci series are 0 and 1 and each next term 
is the sum of the two preceding it. All the Fibonacci numbers calculated in this program must fit
in a unsigned 64 bits number.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

Input
The first line of the input contains a single integer T, indicating the number of test cases. 
Each test case contains a single integer N (0 ≤ N ≤ 60), corresponding to the N-th term of the Fibonacci series.

Output
For each test case in the input, print the message "Fib(N) = X", where X is the N-th term of the Fibonacci series.
'''

a=int(input())
def fibo():
    f=[0,1]
    rep=int(input())
    for x in range (rep):
        n=f[x]+f[x+1]
        f.append(n)
    print("Fib(%i) ="%rep,f[rep])
for y in range (a):      
    fibo()

