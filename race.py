import random

def posizioni(ptar,plep):
    l=["_"]*70
    if ptar!=plep:
        l[ptar-1]="T"
        l[plep-1]="H"
    else:
        l[ptar-1]="OUCH!!!"
    return l

def tartaruga(n,pos):
    if 1<=n<=5:
        return pos+3
    elif 6<=n<=7:
        if pos>6:
            return pos-6
        else:
            return 1
    else:
        return pos+1
def lepre(n,pos):
    if 1<=n<=2:
        return pos
    elif 3<=n<=4:
        return pos+9
    elif n==5:
        if pos>12:
            return pos-12
        else:
            return 1
    elif 6<=n<=8:
        return pos+1
    else:
        if pos>2:
            return pos-2
        else:
            return 1

ptar=1
plep=1
while True:
    n=random.randint(1,10)
    ptar=tartaruga(n,ptar)
    plep=lepre(n,plep)
    if ptar<70 and plep<70:
        print(posizioni(ptar,plep))
    elif ptar>=70 and plep>=70:
        print("ITS A TIE")
        break
    elif ptar>=70:
        print("TORTOISE WINS || VAY!!!")
        break
    else:
        print("HARE WINS || YUCH!!!")
        break