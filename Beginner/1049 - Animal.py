'''
In this problem, your job is to read three Portuguese words. These words define an animal according to 
the table below, from left to right. After, print the chosen animal defined by these three words.

                Ave         Carnivoro   Agua
                            Onivero     Pomba
Vertebrado
                Mamifero    Onivero     Homen
                            Herbivoro   Vaca

                Inseto      Hematofago  Pulga
                            Herbivoro   Largata
Invertebrado
                Analideo    Hematofago  Sanguessuga
                            Onivero     Minhoca

Input
The input contains 3 words, one by line, that will be used to identify the animal, 
according to the above table, with all letters in lowercase.

Output
Print the animal name according to the given input.

Input Samples	
vertebrado
mamifero
onivoro
Output Samples
homem

Input Samples
vertebrado
ave
carnivoro
Output Samples
aguia

Input Samples
invertebrado
anelideo
onivoro
Output Samples
minhoca
'''
dic={"vert":["vertebrado","invertebrado"],"tipo":["ave","mamifero","inseto","anelideo"],"alimento":["carnivoro","onivoro","herbivoro","hematofago"]}
v=input()
t=input()
a=input()
if v==dic["vert"][0]:#Vertebrados
    if t==dic["tipo"][0]:#Ave
        if a==dic["alimento"][0]:#Carnivoro
            print("aguia")
        elif a==dic["alimento"][1]:#Onivero
            print("pomba")
    elif t==dic["tipo"][1]:#mamifero
        if a==dic["alimento"][1]:#Onivoro
            print("homem")
        elif a==dic["alimento"][2]:#herbivoro
            print("vaca")

elif v==dic["vert"][1]:#Invertebrados
    if t==dic["tipo"][2]:#inseto
        if a==dic["alimento"][3]:#hematofago
            print("pulga")
        elif a==dic["alimento"][2]:#herbivoro
            print("largata")
    elif t==dic["tipo"][3]:#anelideo
        if a==dic["alimento"][3]:#hematofago
            print("sanguessuga")
        elif a==dic["alimento"][1]:#Onivero
            print("minhoca")