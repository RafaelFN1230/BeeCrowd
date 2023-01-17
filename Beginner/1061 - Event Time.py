'''
Peter is organizing an event in his University. The event will be in April month, beginning and finishing within April month. The problem is: Peter wants to calculate the event duration in seconds, knowing obviously the begin and the end time of the event.

You know that the event can take from few seconds to some days, so, you must help Peter to compute the total time corresponding to duration of the event.

Input
The first line of the input contains information about the beginning day of the event in the format: “Dia xx”. The next line contains the start time of the event in the format presented in the sample input. Follow 2 input lines with same format, corresponding to the end of the event.

Output
Your program must print the following output, one information by line, considering that if any information is null for example, the number 0 must be printed in place of W, X, Y or Z:

W dia(s)
X hora(s)
Y minuto(s)
Z segundo(s)

Obs: Consider that the event of the test case have the minimum duration of one minute. “dia” means day, “hora” means hour, “minuto” means minute and “Segundo” means second in Portuguese.
'''

dias=0
horas=0
minutos=0
segundos=0
dias_i=0
horas_i=0
minutos_i=0
segundos_i=0
dias_f=0
horas_f=0
minutos_f=0
segundos_f=0

txt,dias_i=input().split()
horas_i,minutos_i,segundos_i=map(int,input().split(":"))
txt,dias_f=input().split()
horas_f,minutos_f,segundos_f=map(int,input().split(":"))
if horas_f<horas_i:
    dias=int(dias_f)-int(dias_i)-1
else:
    dias=int(dias_f)-int(dias_i)
if horas_f<horas_i:
    horas= horas_f-horas_i+24
else:
    horas=horas_f-horas_i
if minutos_f<minutos_i:
    minutos= minutos_f-minutos_i+60
else:
    minutos=minutos_f-minutos_i
if segundos_f<segundos_i:
    segundos= segundos_f-segundos_i+60
else:
    segundos=segundos_f-segundos_i

print("%i dias(s)" %dias)
print("%i hora(s)" %horas)
print("%i minuto(s)" %minutos)
print("%i segundo(s)" %segundos)

