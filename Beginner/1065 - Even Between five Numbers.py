'''
Make a program that reads five integer values. 
Count how many of these values ​​are even and  print this information like the following example.
Input
The input will be 5 integer values.
Output
Print a message like the following example with all letters in lowercase, indicating how many even numbers were typed.
'''
n=0
for x in range (5):
    valor=int(input())
    if (valor%2==0):
        n+=1
print(n,"valores pares")