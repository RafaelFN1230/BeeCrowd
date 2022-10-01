'''
Read an integer N. This N will be the number of integer numbers X that will be read.

Print how many these numbers X are in the interval [10,20] and how many values are out of this interval.
 

Input
The first line of input is an integer N (N < 10000), that indicates the total number of test cases.
Each case is an integer number X (-107 < X < 107).

 

Output
For each test case, print how many numbers are in and how many values are out of the interval.
'''

N=int(input())
dentro=0
fora=0
for y in range (N):
    x=int(input())
    if (x>=10 and x<=20):
        dentro+=1
    else:
        fora+=1

print(dentro,"in")
print(fora,"out")
