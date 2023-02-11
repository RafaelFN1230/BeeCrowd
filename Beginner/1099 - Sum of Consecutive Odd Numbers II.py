'''
Read an integer N that is the number of test cases. 
Each test case is a line containing two integer numbers X and Y. 
Print the sum of all odd values between them, not including X and Y.

Input
The first line of input is an integer N that is the number of test cases that follow. Each test case is a line containing two integer X and Y.

Output
Print the sum of all odd numbers between X and Y.

Input Sample	
7
4   5
13  10
6   4
3   3
3   5
3   4
3   8

Output Sample
0
11
5
0
0
0
12
'''

n=int(input())
for a in range (n):
    x,y=map(int,input().split())
    soma=0
    if x>y:
        while x>y+1:
            x-=1
            if x/2 != x//2:
                soma+=x
        print(soma)
    elif y>x:
        while y>x+1:
            y-=1
            if y/2 != y//2:
                soma+=y
        print(soma)
    elif x==y:
        print(soma)


 