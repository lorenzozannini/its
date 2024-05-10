class Zoo:
    def __init__(self,fences=[],zoo_keepers=[]):
        self.fences=fences
        self.zoo_keepers=zoo_keepers

    def describe_zoo(self):
        r="Guardians:\n\n"
        for guardian in self.zoo_keepers:
            r+=guardian.__str__()+"\n\n"
        r+="Fences:\n\n"
        for fence in self.fences:
            if fence.animals!=[]:
                r+=fence.__str__()
                r+="#"*30+"\n\n"
        return r
 
class Animal:
    def __init__(self,name,species,age,height,width,habitat):
        self.name=name
        self.species=species
        self.age=age
        self.height=height
        self.width=width
        self.preferred_habitat=habitat
        self.health=round(100*(1/age),3)
    
    def __str__(self) -> str:
        return f"(name={self.name}, species={self.species}, age={self.age})"

class Fence:
    def __init__(self,area,temperature,habitat):
        self.area=area
        self.temperature=temperature
        self.tipo_habitat=habitat
        self.animals=[]
        self.maxarea=area
    
    def __str__(self):
        r=f"Fence(area={self.area}, temperature={self.temperature}, habitat={self.tipo_habitat})\n\n"
        r+="with animals:\n\n"
        for animal in self.animals:
            r += animal.__str__()+"\n\n"
        return r

class ZooKeeper:
    def __init__(self,name,surname,id):
        self.name=name
        self.surname=surname
        self.id=id
    
    def __str__(self):
        return f"ZooKeeper(name={self.name}, surname={self.surname}, id={self.id})"

    def add_animal(self,animale):
        count=0
        for fence in zoo.fences:
            if animale in fence.animals:
                break
            else:
                if fence.tipo_habitat ==animale.preferred_habitat:
                    if fence.area>=(animale.height*animale.width):
                        if count==0:
                            fence.animals.append(animale)
                            fence.area-=(animale.height*animale.width)
                            count+=1
                        
    
    def  remove_animal(self,animale):
        for fence in zoo.fences:
            if animale in fence.animals:
                fence.area+=(animale.height*animale.width)
                fence.animals.remove(animale)
    
    def feed(self,animale):
        for fence in zoo.fences:
            if animale in fence.animals:
                for animal in fence.animals:
                    if animal==animale:
                        fence.area+=(animal.height*animal.width)
                        if ((((animal.height)/100)*102)*(((animal.width)/100)*102))<fence.area and (((animal.health)/100)*101)<100:
                            animal.health=(((animal.health)/100)*101)
                            animal.height=round(((animal.height)/100)*102,3)
                            animal.width=round(((animal.width)/100)*102,3)
                            fence.area-=(animal.height*animal.width)
                        else:
                            fence.area-=(animal.height*animal.width)
    
    def clean(self,fence):
        if fence.area==0 or fence.area==fence.maxarea:
            return fence.maxarea
        else:
            tempo=(fence.maxarea-fence.area)/fence.area
            return tempo

z=ZooKeeper(name="Lorenzo", surname="Maggi", id=1234)
f=Fence(area=100, temperature=25, habitat="Continent")
z1=ZooKeeper(name="Lorenzo", surname="Maggi", id=1234)
f1=Fence(area=100, temperature=25, habitat="Continent")
f3=Fence(area=100, temperature=25, habitat="Continent")
f2=[f,f1,f3]
z2=[z,z1]
zoo=Zoo(f2,z2)
scoiattolo=Animal(name="Scoiattolo", species="Blabla", age=25, height=10,width=1,habitat="Continent")
lupo=Animal(name="Lupo", species="Blabla", age=14, height=3,width=8,habitat="Continent")
z.add_animal(scoiattolo)
z.add_animal(lupo)
print(zoo.describe_zoo())
z.add_animal(scoiattolo)
z.feed(scoiattolo)
print(zoo.describe_zoo())
print(z.clean(f))