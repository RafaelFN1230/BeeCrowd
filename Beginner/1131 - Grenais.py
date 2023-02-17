'''
The Federação Gaúcha de Futebol invited you to write a program to present a statistical result of several GRENAIS. 
Write a program that read the number of goals scored by Inter and the number of goals scored by Gremio in a GRENAL. 
Write the message "Novo grenal (1-sim 2-nao)" and request a response. 
If the answer is 1, two new numbers must be read (another input case) asking the number of goals scored 
by the teams in a new departure, otherwise the program must be finished, printing:

- How many GRENAIS were part of the statistics.
- The number of victories of Inter.
- The number of victories of Gremio.
- The number of Draws.
- A message indicating the team that won the largest number of GRENAIS 
(or the message: "Não houve vencedor" if both team won the same quantity of GRENAIS).

Input
The input contains two integer values​​, corresponding to the goals scored by both teams. 
Then there is an integer (1 or 2), corresponding to the repetition of the algorithm.

Output
After each reading of the goals it must be printed the message "Novo grenal (1-sim 2-nao)".
 When the program is finished, the program must print the statistics as the example below.

Input Sample	
3 2
1
2 3
1
3 1
2

Output Sample
Novo grenal (1-sim 2-nao)
Novo grenal (1-sim 2-nao)
Novo grenal (1-sim 2-nao)
3 grenais
Inter:2
Gremio:1
Empates:0
Inter venceu mais
'''
i,g=map(int,input().split())
n=1
vic_i=0
vic_g=0
grenal=0
empates=0
while n==1:
    if i>g:
        vic_i+=1
    elif i<g:
        vic_g+=1
    elif i == 0 and g == 0:
        empates+=1
    grenal+=1
    print("Novo grenal (1-sim 2-nao)")
    n=int(input())
    if n==1:
        i,g=map(int,input().split())
print("%i grenais"%grenal)
print("Inter:%i"%vic_i)
print("Gremio:%i"%vic_g)
print("Empates:%i"%empates)
if vic_i>vic_g:
    print("Inter venceu mais")
elif vic_i<vic_g:
    print("Gremio venceu mais")
elif vic_i==vic_g:
    print("Não houve vencedor")

