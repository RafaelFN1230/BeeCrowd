'''
In this problem you have to read an integer value and calculate the smallest possible number of banknotes in which the value may be decomposed. 
The possible banknotes are 100, 50, 20, 10, 5, 2 e 1. Print the read value and the list of banknotes.

Input
The input file contains an integer value N (0 < N < 1000000).

Output
Print the read number and the minimum quantity of each necessary banknotes in Portuguese language, as the given example. 
Do not forget to print the end of line after each line, otherwise you will receive “Presentation Error”.
'''

valor=int(input())
cem=0
cinquenta=0
vinte=0
dez=0
cinco=0
dois=0
uni=0
if (valor//100!=0):
    cem=valor//100
if((valor-(cem*100))//50!=0):
    cinquenta=(valor-(cem*100))//50
if((valor-(cem*100+cinquenta*50))//20):
    vinte=(valor-(cem*100+cinquenta*50))//20
if((valor-(cem*100+cinquenta*50+vinte*20))//10!=0):
    dez=(valor-(cem*100+cinquenta*50+vinte*20))//10
if((valor-(cem*100+cinquenta*50+vinte*20+dez*10))//5!=0):
    cinco=(valor-(cem*100+cinquenta*50+vinte*20+dez*10))//5
if((valor-(cem*100+cinquenta*50+vinte*20+dez*10+cinco*5))//2!=0):
    dois=(valor-(cem*100+cinquenta*50+vinte*20+dez*10+cinco*5))//2
if((valor-(cem*100+cinquenta*50+vinte*20+dez*10+cinco*5+dois*2))//1!=0):
    uni=(valor-(cem*100+cinquenta*50+vinte*20+dez*10+cinco*5+dois*2))//1


print(cem,"nota(s) de R$ 100,00")
print(cinquenta,"nota(s) de R$ 50,00")
print(vinte,"nota(s) de R$ 20,00")
print(dez,"nota(s) de R$ 10,00")
print(cinco,"nota(s) de R$ 5,00")
print(dois,"nota(s) de R$ 2,00")
print(uni,"nota(s) de R$ 1,00")