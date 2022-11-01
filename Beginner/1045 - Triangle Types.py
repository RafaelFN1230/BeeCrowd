'''
Read 3 double numbers (A, B and C) representing the sides of a triangle and arrange them in decreasing order, 
so that the side A is the biggest of the three sides. Next, determine the type of triangle that they can make, 
based on the following cases always writing an appropriate message:
if A ≥ B + C, write the message: NAO FORMA TRIANGULO
if A2 = B2 + C2, write the message: TRIANGULO RETANGULO
if A2 > B2 + C2, write the message: TRIANGULO OBTUSANGULO
if A2 < B2 + C2, write the message: TRIANGULO ACUTANGULO
if the three sides are the same size, write the message: TRIANGULO EQUILATERO
if only two sides are the same and the third one is different, write the message: TRIANGULO ISOSCELES
Input
The input contains three double numbers, A (0 < A) , B (0 < B) and C (0 < C).

Output
Print all the classifications of the triangle presented in the input.
'''

l1,l2,l3=map(float,input().split())

if l1 >= (l2 + l3) or l2 >= (l1 + l3) or l3 >= (l2 + l1):
    print("NAO FORMA TRIANGULO")
elif l1**2 == (l2**2 + l3**2) or l2**2 == (l1**2 + l3**2) or l3**2 == (l2**2 + l1**2):
    print("TRIANGULO RETANGULO")
elif l1**2 > (l2**2 + l3**2) or l2**2 > (l1**2 + l3**2) or l3**2 > (l2**2 + l1**2):
    print("TRIANGULO OBTUSANGULO")
elif l1**2 < (l2**2 + l3**2) or l2**2 < (l1**2 + l3**2) or l3**2 < (l2**2 + l1**2):
    print("TRIANGULO ACUTANGULO")
if l1==l2 and l2==l3:
    print("TRIANGULO EQUILATERO")
elif l1==l2 or l2==l3 or l1==l3:
    print("TRIANGULO ISOSCELES")