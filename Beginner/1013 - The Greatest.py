'''
Make a program that reads 3 integer values and present the greatest one followed by the message "eh o maior". 

Input
The input file contains 3 integer values.

Output
Print the greatest of these three values followed by a space and the message “eh o maior”.
'''
g=()
g = list(map(int, input().split()))
a=g[0]
for y in g:
    if a<y:
        a=y
print(a,"eh o maior")

