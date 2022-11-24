'''
Read 3 floating-point numbers. After, print the roots of bhaskara’s formula. 
If it's impossible to calculate the roots because a division by zero or a square root of a negative number, 
presents the message “Impossivel calcular”.

Input
Read 3 floating-point numbers (double) A, B and C.

Output
Print the result with 5 digits after the decimal point or the message if it is impossible to calculate.
'''

a,b,c=map(float,input().split())
if a==0 or (b**2)-(4*a*c) <= 0:
    print("Impossivel calcular")
else:
    R1=(-b+((b**2)-(4*a*c))**0.5)/(2*a)
    R2=(-b-((b**2)-(4*a*c))**0.5)/(2*a)
    print("R1 = %.5f"%R1)
    print("R2 = %.5f"%R2)
