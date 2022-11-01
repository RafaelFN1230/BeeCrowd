'''
Read the start time and end time of a game, in hours and minutes 
(initial hour, initial minute, final hour, final minute). 
Then print the duration of the game, knowing that the game can begin in a day and finish in another day,

Obs.: With a maximum game time of 24 hours and the minimum game time of 1 minute.

Input
Four integer numbers representing the start and end time of the game.

Output
Print the duration of the game in hours and minutes, in this format: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” . 
Which means: the game lasted XXX hour(s) and YYY minutes.
'''

s_h,s_m,f_h,f_m=map(int,input().split())

s_t=s_h*60+s_m
f_t=f_h*60+f_m

dura=f_t-s_t

h=dura//60
m=dura-h*60

if h<0:
    dura_f=1440+dura
    h=dura_f//60
    m=dura_f-h*60
if h==0 and m==0:
    h=24
print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)"%(h,m))