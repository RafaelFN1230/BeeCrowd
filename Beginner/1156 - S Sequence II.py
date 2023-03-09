'''
Write an algorithm to calculate and write the value of S, S being given by:
S = 1 + 3/2 + 5/4 + 7/8 + ... + 39/?

Input
There is no input in this problem.

Output
The output contains a value corresponding to the value of S.
The value should be printed with two digits after the decimal point.
'''

def sequence (x,y,s):
    while x<=39:
        s+=(x/y)
        return sequence (x+2,y*2,s)
    print("%.2f"%s)
sequence(1,1,0)