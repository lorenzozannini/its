from abc import ABC, abstractmethod


def carattere(lettera,chiave):
        n_posizione=0
        alphabet={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":12,"l":12,"m":13,"n":14,
                  "o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}
        posizione=alphabet[lettera]
        if posizione+chiave >26:
            n_posizione=(posizione+chiave)-26
        else:
            n_posizione=posizione+chiave
        for k in alphabet:
            if alphabet[k]==n_posizione:
                return k
            
def d_carattere(lettera,chiave):
        n_posizione=0
        alphabet={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":12,"l":12,"m":13,"n":14,
                  "o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}
        posizione=alphabet[lettera]
        if posizione-chiave <0:
            n_posizione=(posizione-chiave)+26
        else:
            n_posizione=posizione-chiave
        for k in alphabet:
            if alphabet[k]==n_posizione:
                return k

def combinazione(testo):
    l1=[]
    l2=[]
    l3=[]
    metà=len(testo)//2
    if len(testo)%2==0:
        for i in range(0,len(testo)):
            if i<metà:
                l1.append(testo[i])
            else:
                l2.append(testo[i])
        for i in range(0,len(l2)):
            l3.append(l1[i])
            l3.append(l2[i])
        return l3
    else:
        for i in range(0,len(testo)):
            if i<=metà:
                l1.append(testo[i])
            else:
                l2.append(testo[i])
        for i in range(0,len(l2)):
            l3.append(l1[i])
            l3.append(l2[i])
        l3.append(l1[-1])
        return l3

def d_combinazione(testo):
    l1=[]
    l2=[]
    l3=[]
    metà=len(testo)//2
    if len(testo)%2==0:
        for i in range(0,len(testo)):
            if i<metà:
                l1.append(testo[i])
            else:
                l2.append(testo[i])
        for i in range(0,len(l2)):
            l3.append(l1[i])
            l3.append(l2[i])
        return l3
    else:
        for i in range(0,len(testo)):
            if i<=metà:
                l1.append(testo[i])
            else:
                l2.append(testo[i])
        for i in range(0,len(l2)):
            l3.append(l1[i])
            l3.append(l2[i])
        l3.append(l1[-1])
        return l3
        
class CodificatoreMessaggio(ABC):
    @abstractmethod
    def codifica(self,testoInChiaro):
        pass

class DecodificatoreMessaggio:
    def decodifica(self,testoCodificato):
        pass

class CifratoreAScorrimento(CodificatoreMessaggio,DecodificatoreMessaggio):
    def __init__(self,chiave):
        self.chiave=chiave
    
    def codifica(self, testoInChiaro):
        l=[]
        for i in testoInChiaro:
            l.append(carattere(i,self.chiave))
        return str(l)
    
    def decodifica(self, testoCodificato):
        l=[]
        for i in testoCodificato:
            l.append(d_carattere(i,self.chiave))
        return str(l)

class CifratoreACombinazione(CodificatoreMessaggio,DecodificatoreMessaggio):
    def __init__(self,n):
        self.n=n
    
    def codifica(self,testoInChiaro):
        for i in range(self.n):
            testoInChiaro=combinazione(testoInChiaro)
        return testoInChiaro
    
    def decodifica(self,testoCodificato):
        for i in range(self.n+1):
            testoCodificato=d_combinazione(testoCodificato)
        return testoCodificato


c1=CifratoreACombinazione(1)
print(c1.codifica("paperino"))
print(c1.decodifica(c1.codifica("paperino")))