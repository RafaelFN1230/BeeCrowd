'''
Write a program that reads an integer N (1 < N < 1000). This N is the number of output lines printed by this program.

Input
The input file contains an integer N.

Output
Print the output according to the given example.

Input Sample
5

Output Sample
1 1 1
2 4 8
3 9 27
4 16 64
5 25 125
'''
n=int(input())
y=1
for a in range (n):
    y=a+1
    x=[str(y),str(y**2),str(y**3)]
    print(' '.join(x))
