class Media:
    def __init__(self):
        self.title=""
        self.reviews=[]
    
    def set_title(self,title):
        self.title=title

    def get_title(self):
        return self.title
    
    def add_reviews(self,voto):
        if voto<=5 and voto>=1:
            self.reviews.append(voto)
        else:
            print("Voto ",voto,"non valido")
        
    def get_media(self):
        return (sum(self.reviews)/len(self.reviews))
    
    def get_rate(self):
        rate=round((sum(self.reviews)/len(self.reviews)))
        if rate==1:
            return("Terribile")
        elif rate ==2:
            return("Brutto")
        elif rate ==3:
            return("Normale")
        elif rate ==4:
            return("Bello")
        elif rate ==5:
            return("Grandioso")

    def rate_percentage(self,voto):
        n=0
        for v in self.reviews:
            if v==voto:
                n+=1
        return (100/len(self.reviews)*n)
        
    def recensione(self):
        s=f"Titolo del Film: {self.get_title()}\n"
        s+=f"Voto Medio: {self.get_media()}\n"
        s+=f"Giudizio: {self.get_rate()}\n"
        s+=f"Terribile: {self.rate_percentage(1)}%\n"
        s+=f"Brutto: {self.rate_percentage(2)}%\n"
        s+=f"Normale: {self.rate_percentage(3)}%\n"
        s+=f"Bello: {self.rate_percentage(4)}%\n"
        s+=f"Grandioso: {self.rate_percentage(5)}%\n"
        return s

class Film(Media):
    def __init__(self,title):
        super().__init__()
        self.set_title(title)


film=Film("Cars")
film.add_reviews(1)
film.add_reviews(2)
film.add_reviews(3)
film.add_reviews(4)
film.add_reviews(4)
film.add_reviews(4)
film.add_reviews(5)
film.add_reviews(5)
film.add_reviews(5)
film.add_reviews(5)
print(film.recensione())

film2=Film("Titanic")
film2.add_reviews(0)
film2.add_reviews(9)
film2.add_reviews(2)
film2.add_reviews(2)
film2.add_reviews(4)
film2.add_reviews(2)
film2.add_reviews(3)
film2.add_reviews(5)
film2.add_reviews(5)
film2.add_reviews(5)
print(film2.recensione())