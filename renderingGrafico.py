from abc import ABC, abstractmethod

class Forma(ABC):

    @abstractmethod
    def getArea(self):
        pass

    @abstractmethod
    def render(self):
        pass

class Quadrato(Forma):
    def __init__(self,lato):
        self.nome="Quadrato"
        self.lato=lato
    
    def getArea(self):
        return self.lato**2
    
    def render(self):
        print("*"*self.lato) 
        for i in range(0,(self.lato)-2):
            print("*",end=" "*(self.lato-2))
            print("*")
        print("*"*self.lato)

class Rettangolo(Forma):
    def __init__(self,base,altezza):
        self.nome="Rettangolo"
        self.base=base
        self.altezza=altezza
    
    def getArea(self):
        return self.altezza*self.base
    
    def render(self):
        print("*"*self.base) 
        for i in range(0,(self.altezza)-2):
            print("*",end=" "*(self.base-2))
            print("*")
        print("*"*self.base)

class Triangolo(Forma):
    def __init__(self,lato):
        self.nome="Triangolo"
        self.altezza=lato
        self.base=lato
    
    def getArea(self):
        return self.base*self.altezza/2
    
    def render(self):
        print("*")
        for i in range(0,self.altezza-1):
            print("*",end=" "*i)
            print("*")
        print("*"*self.base)

q=Quadrato(4)
q.render()
print(q.getArea())
r=Rettangolo(8,4)
r.render()
print(r.getArea())
t=Triangolo(4)
t.render()
print(t.getArea())