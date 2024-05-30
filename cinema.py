class Film:
    def __init__(self,title,duration):
        self.title=title
        self.duration=duration

class Sala:
    def __init__(self,number,film,posti_tot,posti_prenotati=0):
        self.number=number
        self.film=film
        self.posti_tot=posti_tot
        self.posti_prenotati=posti_prenotati

    def prenota_posti(self,num_posti):
        if (self.posti_tot-self.posti_prenotati)>num_posti:
            self.posti_prenotati+=num_posti
            print(f"Posti prenotati con successo")
        else:
            print(f"Numero posti non disponibile")
    
    def posti_disponibili(self):
        return f"Posti disponibili in sala: {self.posti_tot-self.posti_prenotati}"
    
class Cinema:
    def __init__(self):
        self.sale=[]
    
    def aggiungi_sala(self,sala):
        self.sale.append(sala)
    
    def prenota_film(self,titolo_film,num_posti):
        for sala in self.sale:
            if sala.film.title==titolo_film:
                sala.prenota_posti(num_posti)
                return 
        print(f"Film non presente")
    
cinema=Cinema()
cinema.aggiungi_sala(Sala(1,Film("ciao",40),100))
cinema.prenota_film("ciao",40)