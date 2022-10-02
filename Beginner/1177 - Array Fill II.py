'''
Write a program that reads a number T and fill a vector N[1000] with the numbers from 0 to T-1 repeated times, 
like as the example below.

Input
The input contains an integer number T (2 ≤ T ≤ 50).

Output
For each position of the array N, print "N[i] = x", 
where i is the array position and x is the number stored in that position.
'''

cont_T=0
cont=0
N=[]
cont_teste=0
T=int(input())
A=[]

for x in range(T):
    N.append(cont_T)
    cont_T+=1

for y in range(1000):
    print("chegou aqui")
    for z in N:
        print("N[%d] ="%cont,N[z])
        cont+=1
        A.append(z)
    print(cont_teste)
    cont_teste+=1
print(A)