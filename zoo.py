class Zoo:
    def __init__(self,fences=[],zoo_keepers=[]):
        self.fences=[fences]
        self.zoo_keepers=[zoo_keepers]
 
class Animal:
    def __init__(self,name,species,age,height,width,habitat):
        self.name=name
        self.species=species
        self.age=age
        self.height=height
        self.width=width
        self.preferred_habitat=habitat
        self.healt=100*(1/age)
    
    def __str__(self) -> str:
        return f"(Name={self.name}, Species={self.species}, Age={self.age}, Height={self.height})"

class Fence:
    def __init__(self,area,temperature,habitat,animals=[]):
        self.area=area
        self.temperature=temperature
        self.tipo_habitat=habitat
        self.animals=animals
    
    def __str__(self) -> str:
        r=f"(area={self.area})"
        for animal in self.animals:
            r += animal.__str__()+"\n"
        return r

class ZooKeeper:
    def __init__(self,name,surname,id):
        self.name=name
        self.surname=surname
        self.id=id

    def add_animal(self,animale):
        for fence in zoo.fences:
            if animale not in fence.animals:
                if fence.tipo_habitat ==animale.preferred_habitat:
                    if fence.area>=(animale.height*animale.width):
                        fence.animals.append(animale)
                        fence.area-=(animale.height*animale.width)
    
    def  remove_animal(self,animale):
        for fence in zoo.fences:
            if animale in fence.animals:
                fence.animals.remove(animale)
                fence.area+=(animale.height*animale.width)
    
    def feed(self):
        pass
z=ZooKeeper(name="Lorenzo", surname="Maggi", id=1234)
f=Fence(area=100, temperature=25, habitat="Continent")
zoo=Zoo(f,z)
scoiattolo=Animal(name="Scoiattolo", species="Blabla", age=25, height=1,width=2,habitat="Continent")
z.add_animal(scoiattolo)
print(f.__str__())
z.add_animal(scoiattolo)
z.remove_animal(scoiattolo)
print(f.__str__())
