from abc import ABC
class Pagamento(ABC):
    def get(self):
        s=str(self.importo).split(".")
        if len(s[1])<2:
            s[1]+="0"
        else:
            return round(self.importo,2)
        return s[0]+"."+s[1]
         

    def set(self,importo):
        self.importo=float(importo)
    
    def dettagliPagamento(self):
        print(f"Importo del pagamento: €{self.get()}")

class PagamentoContanti(Pagamento):
    def get(self):
        return super().get()
    
    def set(self, importo):
        return super().set(importo)
    
    def dettagliPagamento(self):
        print(f"Pagamento in contanti di: €{self.get()}")
    
    def inPezziDa(self):
        banconote={500:0 , 200:0 , 100:0 , 50:0 , 20:0 , 10:0 , 5:0 , 2:0 , 1:0 , 0.5:0 , 0.2:0 , 0.1:0 , 0.05:0 , 0.01:0}
        imp=self.importo
        while imp>=0.01:
            for i in banconote.keys():
                if i<=imp:
                    imp-=i
                    imp=round(imp,2)
                    banconote[i]+=1
                    break
        for k,v in banconote.items():
            if v>0:
                if k>=5:
                    if v>1:
                        print(f"{v} banconote da {k} euro")
                    else:
                        print(f"{v} banconota da {k} euro")
                else:
                    if v>1:
                        print(f"{v} monete da {k} euro")
                    else:
                        print(f"{v} moneta da {k} euro")

class PagamentoCartaDiCredito(Pagamento):
    def __init__(self,nome,data,numero) -> None:
        self.nome=nome
        self.data=data
        self.numero=numero
    
    def get(self):
        return super().get()
    
    def set(self, importo):
        return super().set(importo)
    
    def dettagliPagamento(self):
        print(f"Pagamento di: €{self.get} effettuato con la carta di credito\n"+
        f"Nome sulla carta: {self.nome}\n"+
        f"Data di scadenza: {self.data}\n"
        f"Numero della carta: {self.numero}")
c=PagamentoContanti()
c.set(95.25)
c.dettagliPagamento()
c.inPezziDa()