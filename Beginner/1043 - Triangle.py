'''
Read three point floating values (A, B and C) and verify if is possible to make a triangle with them. 
If it is possible, calculate the perimeter of the triangle and print the message:


| b - c | < a < b + c
| a - c | < b < a + c
| a - b | < c < a + b

Perimetro = (a+b+c)/2


If it is not possible, calculate the area of the trapezium which basis A and B and C as height, 
and print the message:


Area = ((a+b)*c)/2

Input
The input file has tree floating point numbers.

Output
Print the result with one digit after the decimal point.

Input Sample	
6.0 4.0 2.0
Output Sample
Area = 10.0

Input Sample
6.0 4.0 2.1
Output Sample
Perimetro = 12.1
'''

a,b,c=map(float,input().split())
if abs(b-c) < a and a < b + c and abs(a - c) < b and b < a + c and abs(a - b)< c  and c < a + b:
    p=a+b+c
    print("Perimetro = %.1f"%p)
else:
    area=((a+b)*c)/2
    print("Area = %.1f"%area)

