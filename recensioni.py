class Media:
    def __init__(self):
        self.title=""
        self.reviews=[]
    
    def set_title(self,title):
        self.title=title

    def get_title(self):
        return self.title
    
    def set_reviews(self,voto):
        if voto<=5:
            self.reviews.append(voto)
        else:
            print("Voto non valido")
        
    def get_media(self):
        return (sum(self.reviews)/len(self.reviews))
    
    def get_rate(self):
        rate=round((sum(self.reviews)/len(self.reviews)))
        if rate==1:
            print("Terribile")
        elif rate ==2:
            print("Brutto")
        elif rate ==3:
            print("Normale")
        elif rate ==4:
            print("Bello")
        elif rate ==5:
            print("Grandioso")

    def rate_percentage(self,voto):
        n=0
        if voto in self.reviews:
            for v in self.reviews:
                if v==voto:
                    n+=1
        return (100/len(self.reviews)*n)
    
    def