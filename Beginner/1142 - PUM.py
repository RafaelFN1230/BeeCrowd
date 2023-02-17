'''
Write a program that reads an integer N. This N is the number of output lines printed by this program.

Input
The input file contains an integer N.

Output
Print the output according to the given example.

Input Sample	
7

Output Sample
1 2 3 PUM
5 6 7 PUM
9 10 11 PUM
13 14 15 PUM
17 18 19 PUM
21 22 23 PUM
25 26 27 PUM
'''

n=int(input())
x=[]
z=0
for a in range (n):
    y=[]
    for b in range (4):
        z+=1
        if z%4 == 0:
            y.append("PUM")
        else:
            y.append(str(z))
    x.append(y)
for c in range (n):
    print(' '.join(x[c]))