class MovieCatalog:
    def __init__(self):
        self.catalog={}

    def add_movie(self,director_name,movies):
        if director_name not in self.catalog:
            self.catalog[director_name]=[movies]
        else:
            self.catalog[director_name].append(movies)
    
    def remove_movie(self,director_name,movies):
        self.catalog[director_name].remove(movies)
        if self.catalog[director_name]==[]:
            del self.catalog[director_name]

    def list_directors(self):
        return list(self.catalog.keys())
    
    def get_movie_by_director(self,director_name):
        return self.catalog[director_name]
    
    def serch_movie_by_title(self,title):
        l=[]
        for movies in self.catalog.values():
            for movie in movies:
                if movie[0:len(title)]==title:
                    l.append(movie)
        if l==[]:
            return f"Nessun film presente"
        else:
            return l
catalogo=MovieCatalog()
catalogo.add_movie("ciao","Film1")
catalogo.add_movie("ciao","Film2")
print(catalogo.list_directors())
print(catalogo.get_movie_by_director("ciao"))
print(catalogo.serch_movie_by_title("Film"))