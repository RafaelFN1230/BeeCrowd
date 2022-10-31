'''
Read an integer value, which is the duration in seconds of a certain event in a factory, 
and inform it expressed in hours:minutes:seconds.

Input
The input file contains an integer N.

Output
Print the read time in the input file (seconds) converted in hours:minutes:seconds like the following example.
'''

x = int (input())

h=x//3600
m=(x-(3600*h))//60
s=x-(3600*h)-(60*m)

print("%i:%i:%i"%(h,m,s))