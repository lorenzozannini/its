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
        for movies in self.catalog.values():
            for movie in movies:
                if title in movie:
                    return movie
        return f"Nessun film presente"
catalogo=MovieCatalog()
catalogo.add_movie("ciao","300")
catalogo.add_movie("ciao","Il buco")
print(catalogo.list_directors())
print(catalogo.get_movie_by_director("ciao"))
print(catalogo.serch_movie_by_title("buco"))