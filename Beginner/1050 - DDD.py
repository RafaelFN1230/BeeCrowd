'''
Read an integer number that is the code number for phone dialing. 
Then, print the destination according to the following table:

61 Brasilia
71 Salvador
11 São Paulo
21 Rio de Janeiro
32 Juiz de Fora
19 Campinas
27 Vitoria
31 Belo Horizonte


If the input number isn’t found in the above table, the output must be:
DDD nao cadastrado
That means “DDD not found” in Portuguese language.

Input
The input consists in a unique integer number.  

Output
Print the city name corresponding to the input DDD. Print DDD nao cadastrado 
if doesn't exist corresponding DDD to the typed number.
'''

ddd=[[61,71,11,21,32,19,27,31],["Brasilia", "Salvador", "Sao Paulo", "Rio de Janeiro", "Juiz de Fora", "Campinas", "Vitoria", "Belo Horizonte"]]
cont=0
resp=0
n=int(input())

for x in ddd[0]:
    if n==x:
        resp=cont
    cont+=1
 
if ddd[0][resp]==n:
    print(ddd[1][resp])   
else:
    print("DDD nao cadastrado") 
