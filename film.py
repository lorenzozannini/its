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
    

catalogo=MovieCatalog()
catalogo.add_movie("ciao","2")
print(catalogo.list_directors())
catalogo.remove_movie("ciao","2")
print(catalogo.list_directors())