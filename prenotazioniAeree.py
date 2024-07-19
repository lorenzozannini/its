from abc import ABC,abstractmethod

class Volo(ABC):
    @abstractmethod
    def __init__(self,codice,posti):
        self.codice=codice
        self.posti_totali=posti
        self.prenotazioni=0

    @abstractmethod
    def prenota_posto(self):
        pass

    @abstractmethod
    def posti_disponibili(self):
        pass

class VoloCommerciale(Volo):
    def __init__(self, codice, posti):
        super().__init__(codice, posti)
        p_posto=self.posti_totali//100
        self.posti_economica=p_posto*70
        self.posti_business=p_posto*20
        self.posti_prima=self.posti_totali-(self.posti_business+self.posti_economica)
        self.prenotazioni_economica=0
        self.prenotazioni_business=0
        self.prenotazioni_prima=0
    
    def prenota_posto(self,posti,classe_servizio):
        if self.posti_totali>posti:
            if classe_servizio=="economica":
                if self.posti_economica>posti:
                    self.posti_economica-=posti
                    self.prenotazioni+=posti
                    print(f"Riservati {posti} posti nella {classe_servizio} classe per il volo {self.codice}")
                else:
                    print(f"Numero posti non disponibili nella {classe_servizio} classe")
            elif classe_servizio=="business":
                if self.posti_business>posti:
                    self.posti_business-=posti
                    self.prenotazioni+=posti
                    print(f"Riservati {posti} posti nella {classe_servizio} classe per il volo {self.codice}")
                else:
                    print(f"Numero posti non disponibili nella {classe_servizio} classe")
            elif classe_servizio=="prima":
                if self.posti_prima>posti:
                    self.posti_prima-=posti
                    self.prenotazioni+=posti
                    print(f"Riservati {posti} posti nella {classe_servizio} classe per il volo {self.codice}")
                else:
                    print(f"Numero posti non disponibili nella {classe_servizio} classe")
            else:
                print("Classe non corretta")
        else:
            print("Non ci sono abbastanza posti disponibili")
    
    def posti_disponibili(self):
        return {"posti disponibili":self.posti_totali-self.prenotazioni,"classe economica":self.posti_economica-self.prenotazioni_economica,"classe business":self.posti_business-self.prenotazioni_business,"prima classe":self.posti_prima-self.prenotazioni_prima}

class VoloCharter(Volo):
    def __init__(self, codice, posti,costo):
        super().__init__(codice, posti)
        self.costo=costo
    
    def prenota_posto(self):
        if self.prenotazioni==0:
            self.prenotazioni+=self.posti_totali
            print(f"Volo {self.codice} prenotato al prezzo di {self.costo}€")
        else:
            print("Volo già prenotato")
    
    def posti_disponibili(self):
        return self.posti_totali
    
class CompagniaAerea:
    def __init__(self,nome,prezzo):
        self.nome=nome
        self.prezzo=prezzo
        self.flotta=[]
    
    def aggiungi_volo(self,volo_commericiale):
        if volo_commericiale not in self.flotta:
            self.flotta.append(volo_commericiale)
        else:
            print("Volo già presente")
    
    def rimuovi_volo(self,volo_commerciale):
        if volo_commerciale in self.flotta:
            self.flotta.remove(volo_commerciale)
        else:
            print("Volo non presente")
    
    def mostra_flotta(self):
        print("Voli:")
        for v in self.flotta:
            print(v.codide)

    def guadagno(self):
        g=0
        for v in self.flotta:
            if isinstance(v,VoloCommerciale)==True:
                g+=((v.posti_economica*self.prezzo)+v.posti_business*(self.prezzo*2)+v.posti_prima*(self.prezzo*3))
            else:
                g+=v.costo
        return g

vc=VoloCharter("CHA456",200,20000)
vcom=VoloCommerciale("COM123",100)
vcom.prenota_posto(20,"economica")
print(vcom.posti_disponibili())
compagnia=CompagniaAerea("c",20)
compagnia.aggiungi_volo(vc)
compagnia.aggiungi_volo(vcom)
compagnia.rimuovi_volo(vc)
print(compagnia.guadagno())