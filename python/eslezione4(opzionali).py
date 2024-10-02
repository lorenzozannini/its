#1
import random


def school(n,*score):
    average=sum(score)/len(score)
    if average>=60:
        return "Lo studente",n,"è promosso con",average
    else:
        return "Lo studente",n,"è bocciato con",average
print(school("Mattia",60,60,60,60))
print(school("Marco",0,0,0,0))

#2
def number_game(n):
    i=0
    n=random.randint(0,n)
    while i<10:
        num=int(input("Inserisci prova->"))
        if n==num:
            return "Complimenti hai vinto"
        else:
            if n>num:
                if n-num<10:
                    print("Ci sei andato vicino")
                else:
                    print("Non ci sei proprio")
            else:
                if num-n<10:
                    print("Ci sei andato vicino")
                else:
                    print("Non ci sei proprio")
        i+=1
    return "tentativi esauriti"
print(number_game(3))

#3
def shopping_cart():
    