class Prodotto:
    def __init__(self,nome,quantita):
        self.nome=nome
        self.quantita=quantita

class Magazzino:
    def __init__(self):
        self.prodotti=[]
    
    def aggiungi_prodotto(self,prodotto):
        self.prodotti.append(prodotto)
    
    def cerca_prodotto(self,nome):
        for prodotto in self.prodotti:
            if prodotto.nome==nome:
                return prodotto.nome
    
    def verifica_disponibilita(self,nome):
        for prodotto in self.prodotti:
            if prodotto.nome==nome and prodotto.quantita>0:
                return f"{nome} disponibile in magazzino"
        return f"{nome} non disponibile in magazzino"
            
magazzino=Magazzino()
magazzino.aggiungi_prodotto(Prodotto("salame",0))
magazzino.aggiungi_prodotto(Prodotto("tonno",10))
print(magazzino.cerca_prodotto("salame"))
print(magazzino.cerca_prodotto("tonno"))
print(magazzino.verifica_disponibilita("salame"))
print(magazzino.verifica_disponibilita("tonno"))