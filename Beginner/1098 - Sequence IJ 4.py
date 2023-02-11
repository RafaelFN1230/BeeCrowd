'''
Make a program that prints the sequence like the following example.

Input
This problem doesn't have input.

Output
Print the sequence like the example below.

Input Sample	Output Sample
I=0 J=1
I=0 J=2
I=0 J=3
I=0.2 J=1.2
I=0.2 J=2.2
I=0.2 J=3.2
.....
I=2 J=?
I=2 J=?
I=2 J=?
'''

i=0
j=1
for x in range (11):
    for y in range (3):
        txt = "I={:n} J={:n}"
        print(txt.format(i,j))
        j+=1
    i+=0.2
    j-=2.8
    
    