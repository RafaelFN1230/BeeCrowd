'''
Read two integer values (A and B). After, the program should print the message "Sao Multiplos" (are multiples) 
or "Nao sao Multiplos" (aren’t multiples), corresponding to the read values.

Input
The input has two integer numbers.

Output
Print the relative message to the input as stated above.

Input Sample	
6 24
Output Sample
Sao Multiplos

Input Sample
6 25
Output Sample
Nao sao Multiplos
'''

x,y=map(int,input().split())

if y%x==0 or x%y==0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")