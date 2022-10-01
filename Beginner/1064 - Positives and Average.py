'''
Read 6 values that can be floating point numbers. After, print how many of them were positive. 
In the next line, print the average of all positive values typed, with one digit after the decimal point.

Input
The input consist in 6 numbers that can be integer or floating point values. At least one number will be positive.

Output
The first output value is the amount of positive numbers. The next line should show the average of the positive values ​typed.
'''
media=0
soma=0
cont=0
for x in range (6):
    n=float(input())
    if(n>0):
        soma+=n
        cont+=1
media=soma/cont
print(cont,"valores positivos")
print("%.1f"%media)