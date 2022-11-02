'''
Read three integers and sort them in ascending order. 
After, print these values in ascending order, 
a blank line and then the values in the sequence as they were readed.

Input
The input contains three integer numbers.

Output
Present the output as requested above.


Input Sample	
7 21 -14

Output Sample
-14
7
21

7
21
-14

Input Sample
-14 21 7

Output Sample
-14
7
21

-14
21
7
'''

n=list(map(int,input().split()))

n_o=n.copy()
n_o.sort()
for x in n_o:
    print(x)
print("")
for y in n:
    print(y)
