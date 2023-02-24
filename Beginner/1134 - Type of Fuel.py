'''
A gas station wants to determine which of their products is the preference of their customers. 
Write a program to read the type of fuel supplied 
(coded as follows: 1. Alcohol 2. Gasoline 3. Diesel 4. End). 
If you enter an invalid code (outside the range of 1 to 4) a new code must be requested. 
The program will end when the inserted code is the number 4.

Input
The input contains only integer and positive values.

Output
It should be written the message: "MUITO OBRIGADO" and the amount of customers who fueled each fuel type, as an example.

Input Sample	
8
1
7
2
2
4

Output Sample
MUITO OBRIGADO
Alcool: 1
Gasolina: 2
Diesel: 0
'''

n=int(input())
a=0
g=0
d=0
y=0
for x in range (n):
    while y!=4:
        y=int(input())
        if y ==1:
            a+=1
        elif y ==2:
            g+=1
        elif y ==3:
            d+=1
        elif y ==4:
            pass
print("MUITO OBRIGADO")
print("Alcool: %i"%a)
print("Gasolina: %i"%g)
print("Diesel: %i"%d)
