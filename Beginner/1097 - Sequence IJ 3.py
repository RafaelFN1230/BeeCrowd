'''
Make a program that prints the sequence like the following exemple.

Input
This problem doesn't have input.

Output
Print the sequence like the example below.

Input Sample	Output Sample
I=1 J=7
I=1 J=6
I=1 J=5
I=3 J=9
I=3 J=8
I=3 J=7
...
I=9 J=15
I=9 J=14
I=9 J=13
'''
i=1
j=7
for x in range (5):
    for y in range (3):
        print("I=%i J=%i" %(i,j))
        j-=1
    j+=5
    i+=2
