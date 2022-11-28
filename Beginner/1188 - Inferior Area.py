'''
Read an uppercase character that indicates an operation that will be performed in an array M[12][12]. 
Then, calculate and print the sum or average considering only that numbers that are included in the green area of 
this array, like shown in the following figure.




Input
The first line of the input contains a single uppercase character O ('S' or 'M'), 
indicating the operation Sum or Average (Média in portuguese) to be performed with the elements of the array. 
Follow 144 floating-point numbers (double) of the array.

Output
Print the calculated result (sum or average), with one digit after the decimal point.
'''

letra=input()
resp=0
m=[[],[],[],[],[],[],[],[],[],[],[],[]]
for l in range (12):
    for c in range (12):
        num=float(input())
        m[l].append(num)

cont=0
media=0
index=len(m)-1
linha=len(m)
minimo=linha//2
maximo=linha//2
if (index//2 != index/2):
    linha+=1
    minimo-=1

for x in m[linha//2+1:]:   
    for y in x:
        if cont>=minimo and cont<=maximo:
            resp+=y
            media+=1 
        cont+=1
    index-=1
    minimo-=1
    maximo+=1
    cont=0
if letra=="M":
    resp/=media
print("%.1f"%resp)