'''
Maria has just started as graduate student in a medical school and she's needing your help to organize 
a laboratory experiment which she is responsible about. She wants to know, at the end of the year,
how many animals were used in this laboratory and the percentage of each type of animal is used at all.

This laboratory uses in particular three types of animals: frogs, rats and rabbits. 
To obtain this information, it knows exactly the number of experiments that were performed, 
the type and quantity of each animal is used in each experiment.

Input
The first line of input contains an integer N indicating the number of test cases that follows. 
Each test case contains an integer Amount (1 ≤ Amount ≤ 15) which represents the amount of animal 
used and a character Type ('C', 'R' or 'S'), indicating the type of animal:
- C: Coelho (rabbit in portuguese)
- R: Rato (rat  in portuguese)
- S: Sapo (frog in portuguese)

Output
Print the total of animals used, the total of each type of animal and the percentual of 
each one in relation of the total of animals used. The percentual must be printed with 2 digits 
after the decimal point.
'''
c=0
r=0
s=0

n=int(input())

for x in range (n):
    a,b=input().split()
    if b=="C":
        c+=int(a)

    elif b=="R":
        r+=int(a)
    else:
        s+=int(a)
total=c+r+s
percent_c=c/total*100
print(percent_c)
percent_r=r/total*100
percent_s=s/total*100
print("Total: %i cobaias" %total)
print("Total de coelhos: %i" %c)
print("Total de ratos: %i" %r)
print("Total de sapos: %i" %s)
print("Percentual de coelhos:%.2f" %percent_c,"%")
print("Percentual de ratos:%.2f" %percent_r,"%")
print("Percentual de sapos:%.2f" %percent_s,"%")


