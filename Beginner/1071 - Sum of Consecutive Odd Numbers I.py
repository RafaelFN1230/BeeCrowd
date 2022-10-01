'''
Read two integer values X and Y. Print the sum of all odd values between them.

Input
The input file contain two integer values.

Output
The program must print an integer number. 
This number is the sum off all odd values between both input values that must fit in an integer number.
'''

x=int(input())
y=int(input())

soma=0
if (x>y):
    for n in range (y+1,x):
        if (n%2!=0):
            soma+=n
elif (x<y):
    for n in range (x+1,y):
            if (n%2!=0):
                soma+=n
print(soma)