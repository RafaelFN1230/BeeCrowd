'''
The company ABC decided to give a salary increase to its employees, according to the following table:


Salary	                Readjustment Rate
0 - 400.00              15%
400.01 - 800.00         12%
800.01 - 1200.00        10%
1200.01 - 2000.00       7%
Above 2000.00           4%



Read the employee's salary, calculate and print the new employee's salary, as well the money earned and the increase percentual obtained by the employee, with corresponding messages in Portuguese, as the below example.
Input
The input contains only a floating-point number, with 2 digits after the decimal point.

Output
Print 3 messages followed by the corresponding numbers (see example) informing the new salary, the among of money earned (both must be shown with 2 decimal places) and the percentual obtained by the employee. Note:
Novo salario:  means "New Salary"
Reajuste ganho: means "Money earned"
Em percentual: means "In percentage"

Input Sample	
400.00
Output Sample
Novo salario: 460.00
Reajuste ganho: 60.00
Em percentual: 15 %

Input Sample
800.01
Output Sample
Novo salario: 880.01
Reajuste ganho: 80.00
Em percentual: 10 %

Input Sample
2000.00
Output Sample
Novo salario: 2140.00
Reajuste ganho: 140.00
Em percentual: 7 %
'''

s_i=float(input())

if s_i>0 and s_i<=400:
    s_f=s_i*1.15
    dif=s_f-s_i
    print("Novo salario: %.2f"%s_f)
    print("Reajuste ganho: %.2f"%dif)
    print("Em percentual: 15 %")
elif s_i>400 and s_i<=800:
    s_f=s_i*1.12
    dif=s_f-s_i
    print("Novo salario: %.2f"%s_f)
    print("Reajuste ganho: %.2f"%dif)
    print("Em percentual: 12 %")
elif s_i>800 and s_i<=1200:
    s_f=s_i*1.10
    dif=s_f-s_i
    print("Novo salario: %.2f"%s_f)
    print("Reajuste ganho: %.2f"%dif)
    print("Em percentual: 10 %")
elif s_i>1200 and s_i<=2000:
    s_f=s_i*1.07
    dif=s_f-s_i
    print("Novo salario: %.2f"%s_f)
    print("Reajuste ganho: %.2f"%dif)
    print("Em percentual: 7 %")
elif s_i>2000:
    s_f=s_i*1.04
    dif=s_f-s_i
    print("Novo salario: %.2f"%s_f)
    print("Reajuste ganho: %.2f"%dif)
    print("Em percentual: 4 %")