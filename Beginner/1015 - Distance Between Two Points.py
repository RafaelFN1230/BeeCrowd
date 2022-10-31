'''
Read the four values corresponding to the x and y axes of two points in the plane, 
p1 (x1, y1) and p2 (x2, y2) and calculate the distance between them, showing four decimal places after the comma.

Input
The input file contains two lines of data. The first one contains two double values: 
x1 y1 and the second one also contains two double values with one digit after the decimal point: x2 y2.

Output
Calculate and print the distance value using the provided formula, with 4 digits after the decimal point.
'''

p=[[],[]]
for a in range (2):
    x,y=list(map(float,input().split()))
    p[0].append(x)
    p[1].append(y)
resp=((p[0][1]-p[0][0])**2+(p[1][1]-p[1][0])**2)**(1/2)
print("%.4f"%resp)
