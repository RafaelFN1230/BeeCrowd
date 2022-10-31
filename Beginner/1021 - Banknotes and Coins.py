'''
Read a value of floating point with two decimal places. This represents a monetary value. 
After this, calculate the smallest possible number of notes and coins on which the value can be decomposed. 
The considered notes are of 100, 50, 20, 10, 5, 2. The possible coins are of 1, 0.50, 0.25, 0.10, 0.05 and 0.01. 
Print the message “NOTAS:” followed by the list of notes and the message “MOEDAS:” 
followed by the list of coins.
	
NOTAS:
nota(s) de R$ 100.00
nota(s) de R$ 50.00
nota(s) de R$ 20.00
nota(s) de R$ 10.00
nota(s) de R$ 5.00
nota(s) de R$ 2.00
MOEDAS:
moeda(s) de R$ 1.00
Moeda(s) de R$ 0.50
moeda(s) de R$ 0.25
moeda(s) de R$ 0.10
moeda(s) de R$ 0.05
moeda(s) de R$ 0.01

Input
The input file contains a value of floating point N (0 ≤ N ≤ 1000000.00).

Output
Print the minimum quantity of banknotes and coins necessary to change the initial value, 
as the given example.
'''

n=float(input())

cem=n//100
cinquenta=(n-(100*cem))//50
vinte=(n-(100*cem)-(50*cinquenta))//20
dez=(n-(100*cem)-(50*cinquenta)-(20*vinte))//10
cinco=(n-(100*cem)-(50*cinquenta)-(20*vinte)-(10*dez))//5
dois=(n-(100*cem)-(50*cinquenta)-(20*vinte)-(10*dez)-(5*cinco))//2
m_um=(n-(100*cem)-(50*cinquenta)-(20*vinte)-(10*dez)-(5*cinco)-(2*dois))//1
m_cinquenta=(n-(100*cem)-(50*cinquenta)-(20*vinte)-(10*dez)-(5*cinco)-(2*dois)-(1*m_um))//0.5
m_vc=(n-(100*cem)-(50*cinquenta)-(20*vinte)-(10*dez)-(5*cinco)-(2*dois)-(1*m_um)-(0.5*m_cinquenta))//0.25
m_dez=(n-(100*cem)-(50*cinquenta)-(20*vinte)-(10*dez)-(5*cinco)-(2*dois)-(1*m_um)-(0.5*m_cinquenta)-(0.25*m_vc))//0.1
m_cinco=(n-(100*cem)-(50*cinquenta)-(20*vinte)-(10*dez)-(5*cinco)-(2*dois)-(1*m_um)-(0.5*m_cinquenta)-(0.25*m_vc)-(0.1*m_dez))//0.05
m_cent=(n-(100*cem)-(50*cinquenta)-(20*vinte)-(10*dez)-(5*cinco)-(2*dois)-(1*m_um)-(0.5*m_cinquenta)-(0.25*m_vc)-(0.1*m_dez)-(0.05*m_cinco))//0.01
print("NOTAS:")
print("%.0f nota(s) de R$ 100.00"%cem)
print("%.0f nota(s) de R$ 50.00"%cinquenta)
print("%.0f nota(s) de R$ 20.00"%vinte)
print("%.0f nota(s) de R$ 10.00"%dez)
print("%.0f nota(s) de R$ 5.00"%cinco)
print("%.0f nota(s) de R$ 2.00"%dois)
print("MOEDAS:")
print("%.0f moeda(s) de R$ 1.00"%m_um)
print("%.0f moeda(s) de R$ 0.50"%m_cinquenta)
print("%.0f moeda(s) de R$ 0.25"%m_vc)
print("%.0f moeda(s) de R$ 0.10"%m_dez)
print("%.0f moeda(s) de R$ 0.05"%m_cinco)
print("%.0f moeda(s) de R$ 0.01"%m_cent)
