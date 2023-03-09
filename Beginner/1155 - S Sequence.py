'''
Write an algorithm to calculate and write the value of S, S being given by:
S = 1 + 1/2 + 1/3 + … + 1/100

Input
There is no input in this problem.

Output
The output contains a value corresponding to the value of S.
The value should be printed with two digits after the decimal point.
'''
def sequence(s,x):
    while s<=100:
        r=1/s
        x+=r
        return sequence (s+1,x)
    print("%.2f"%x)  
sequence(1,0)