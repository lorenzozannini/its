#9.1
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.name=restaurant_name
        self.type=cuisine_type
    def describe_restaurant(self):
        print(f"(name={self.name}, type={self.type})")
    def open_restaurant(self):
        print(self.name,"APERTO!")
    
ristorante=Restaurant("Sole" ,"Rosso")
ristorante.describe_restaurant()
ristorante.open_restaurant()

#9.2
ristorante1=Restaurant("Luna","Giallo")
ristorante2=Restaurant("Orso","Nero")
ristorante3=Restaurant("Salame","Bianco")
ristorante1.describe_restaurant()
ristorante2.describe_restaurant()
ristorante3.describe_restaurant()

#9.3
class User:
    def __init__(self,first_name,last_name,age):
        self.f_name=first_name
        self.l_name=last_name
        self.age=age
    def describe_user(self): 
        print(f"(first name={self.f_name}, last name={self.l_name}, age={self.age})")
    def greet_user(self):
        