'''
Write a program that reads 6 numbers. These numbers will only be positive or negative (disregard null values). 
Print the total number of positive numbers.

Input
Six numbers, positive and/or negative.

Output
Print a message with the total number of positive numbers.
'''

positive=0
for x in range (6):
    n=float(input())
    if (n>0):
        positive+=1
    
print(positive,"valores positivos")