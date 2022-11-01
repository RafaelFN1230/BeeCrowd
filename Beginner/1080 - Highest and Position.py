'''
Read 100 integer numbers. Print the highest read value and the input position.

Input
The input file contains 100 distinct positive integer numbers.

Output
Print the highest number read and the input position of this value, according to the given example.
'''

a=[]
for x in range(100):
    n=int(input())
    a.append(n)
    resp=a[0]
cont=0
for y in a:
    cont+=1
    if resp<y:
        resp=y
        resp_cont=cont
    

print(resp)
print(resp_cont)