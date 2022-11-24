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
m=[[1,2,3,4,5,6,7],[8,9,10,11,12,13,14],[15,16,17,18,19,20,21],[22,23,24,25,26,27,28],[29,30,31,32,33,34,35],[36,37,38,39,40,41,42],[43,44,45,46,47,48,49]]
'''for l in range (12):
    for c in range (12):
        num=float(input())
        m[l].append(num)'''

cont=0
media=0
index=len(m)-1
linha=len(m)
minimo=linha//2
maximo=linha//2
print(index)
if (index//2 != index/2):
    linha+=1
    minimo-=1

for x in m[linha//2+1:]:   
    for y in x:
        print("Y: ",y)
        if cont>=minimo and cont<=maximo:
            resp+=y
            media+=1 
        print("MAX: ",maximo)
        print("MIN: ",minimo)
        print("RESP: ",resp)
        print("CONT: ",cont)
        print("INDEX: ",index) 
        cont+=1
    index-=1
    minimo-=1
    maximo+=1
    cont=0
if letra=="M":
    resp/=media
print("%.1f"%resp)