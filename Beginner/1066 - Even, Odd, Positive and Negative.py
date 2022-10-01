'''
Make a program that reads five integer values. Count how many of these values are even, odd, positive and negative. 
Print these information like following example.

Input
The input will be 5 integer values.

Output
Print a message like the following example with all letters in lowercase, 
indicating how many of these values ​​are even, odd, positive and negative.
'''

par=0
impar=0
posi=0
neg=0

for x in range(5):
    n=int(input())
    if(n<0):
        neg+=1
    elif(n>0):
        posi+=1
    if(n%2==0):
        par+=1
    elif(n%2!=0):
        impar+=1
print(par,"valor(es) par(es)")
print(impar,"valor(es) impar(es)")
print(posi,"valor(es) positivo(s)")
print(neg,"valor(es) negativo(s)")
 