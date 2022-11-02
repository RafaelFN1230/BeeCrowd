'''
Write an algorithm that reads two floating values (x and y), 
which should represent the coordinates of a point in a plane. 
Next, determine which quadrant the point belongs,
or if you are at one of the Cartesian axes or the origin (x = y = 0).

Q2 / Q1
---+---
Q3 / Q4

If the point is at the origin, write the message "Origem".

If the point is at X axis write "Eixo X", else if the point is at Y axis write "Eixo Y".

Input
The input contains the coordinates of a point.

Output
The output should display the quadrant in which the point is.
'''

x,y=map(float,input().split())

if x>0:
    if y>0:
        print("Q1")
    elif y<0:
        print("Q4")
elif x<0:
    if y>0:
        print("Q2")
    elif y<0:
        print("Q3")
elif x==0 and y==0:
    print("Origem")
if x==0 and y!=0:
    print("Eixo Y")
if x!=0 and y==0:
    print("Eixo X")