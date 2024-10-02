import random

def posizioni(ptar,plep):
    l=["_"]*70
    if ptar!=plep:
        l[ptar-1]="T"
        l[plep-1]="H"
    else:
        l[ptar-1]="OUCH!!!"
    return l

def tartaruga(n,pos,sole,e):
    if sole==True:
        if 1<=n<=5:
            if e>=5:
                return pos+3,e-5
            else:
                return pos,e+10
        elif 6<=n<=7:
            if e>=10:
                if pos>6:
                    return pos-6,e-10
                else:
                    return 1,e-10
            else:
                return pos,e+10
        else:
            if e>=3:   
                return pos+1,e-3
            else:
                return pos,e+10
    else:
        pos-=1
        if 1<=n<=5:
            if e>=5:
                return pos+3,e-5
            else:
                return pos,e+10
        elif 6<=n<=7:
            if e>=10:
                if pos>6:
                    return pos-6,e-10
                else:
                    return 1,e-10
            else:
                return pos,e+10
        else:
            if e>=3:   
                return pos+1,e-3
            else:
                return pos,e+10

def lepre(n,pos,sole,e):
    if sole==True:
        if 1<=n<=2:
            if e+10>100:
                return pos,e==100
            else:
                return pos,e+10
        elif 3<=n<=4:
            if e>=15:
                return pos+9,e-15
            else:
                return pos,e
        elif n==5:
            if e>=20:
                if pos>12:
                    return pos-12,e-20
                else:
                    return 1,e-20
            else:
                return pos,e
        elif 6<=n<=8:
            if e>=5:
                return pos+1,e-5
            else:
                return pos,e
        else:
            if e>=8:
                if pos>2:
                    return pos-2,e-8
                else:
                    return 1,e-8
            else:
                return pos,e
    else:
        pos-=2
        if 1<=n<=2:
            if e+10>100:
                return pos,e==100
            else:
                return pos,e+10
        elif 3<=n<=4:
            if e>=15:
                return pos+9,e-15
            else:
                return pos,e
        elif n==5:
            if e>=20:
                if pos>12:
                    return pos-12,e-20
                else:
                    return 1,e-20
            else:
                return pos,e
        elif 6<=n<=8:
            if e>=5:
                return pos+1,e-5
            else:
                return pos,e
        else:
            if e>=8:
                if pos>2:
                    return pos-2,e-8
                else:
                    return 1,e-8
            else:
                return pos,e
bonusmalus={10:3,15:-3,20:5,25:-5,40:10,50:-10}
i=0
ptar=1
plep=1
etar=100
elep=100
sole=True
while True:
    n=random.randint(1,10)
    ptar,etar=tartaruga(n,ptar,sole,etar)
    plep,elep=lepre(n,plep,sole,elep)
    if ptar in bonusmalus:
        ptar+=bonusmalus[ptar]
    if plep in bonusmalus:
        plep+=bonusmalus[plep]
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
    if i%10==0:
        sole=not sole
    i+=1