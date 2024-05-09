"""
#1
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.hobby=[]
    def __str__(self) -> str:
        return f"(name={self.name},age={self.age})"
    def add_hobby(self,hobby):
        self.hobby.append(hobby)
    def remove_hobby(self,oldhobby):
        if oldhobby in self.hobby:
            self.hobby.remove(oldhobby)
    def add_more_hobby(self,l):
        self.hobby+=l

alice=Person("Alice W.",45)
bob=Person("Bob M.",36)
print(bob.age)
if bob.age>alice.age:
    print("Bob is older then Alice")
else:
    print("Alice is older then Bob")
pippo=Person("Pippo C.",14)
marco=Person("Marco M.",86)
sara=Person("Sara M.",76)
people=[alice,bob,pippo,marco,sara]
min=alice.age
k=0
for i in range(0,len(people)):
    if people[i].age<min:
        min=people[i].age
        k=i
people[k].add_hobby("ciao")
print(people[k].hobby)
people[k].add_more_hobby(["calcio","auto","sale"])
print(people[k].hobby)
people[k].remove_hobby("ciao")
print(people[k].hobby)

#2
class Student:
    def __init__(self,name,studyProgram,age,gender):
        self.name=name
        self.studyProgram=studyProgram
        self.age=age
        self.gender=gender

    def printInfo(self):
        print(f"(Name={self.name}, Study program={self.studyProgram}, Age={self.age}, Gender={self.gender})")

s1=Student("Lorenzo",10,19,"M")
s2=Student("Davide",7,19,"M")
s3=Student("Munir",9,23,"M")
s3.printInfo()

#3
class Animals:
    def __init__(self,name,legs):
        self.name=name
        self.legs=legs
    def setLegs(self,n):
        self.legs=n
    def getLegs(self):
        return self.legs
    def printInfo(self):
        print(f"(Name={self.name}, Legs={self.legs})")

cat=Animals("Cat",4)
dog=Animals("Dog",4)
print(cat.name)
print(dog.name)
cat.legs=5
print(cat.legs)
cat.setLegs(7)
print(cat.legs)
print(cat.getLegs())
cat.printInfo()
"""
#4
class Food:
    def __init__(self,name,price,description):
        self.name=name
        self.price=price
        self.description=description

pizza=Food("Pizza",10,"aaaa")
pasta=Food("Pasta",8,"bbbbb")
panino=Food("Panino",5,"ccc")
foods=[pizza,pasta,panino]
class Menu:
    def __init__(self,foods=[]):
        self.foods=foods
    def addFood(self,addfood):
        count=0
        for i in self.foods:
            if addfood.name ==i.name:
                i.price=addfood.price
                count+=1
        if count==0:
            self.foods.append(addfood)
    def removeFood(self,removefood):
         if removefood in self.foods:
            self.foods.remove(removefood)
    def printInfo(self):
        print("Menu:")
        for i in self.foods:
            print(f"(Name={i.name}, Price={i.price}, Description={i.description})")
    def getAveragePrice(self):
        somma=0
        average=0
        for i in self.foods:
            somma+=i.price
        average=somma/len(self.foods)
        return average
menu=Menu(foods)
print(menu.printInfo())
menu.addFood(Food("Sale",3,"dddd"))
print(menu.printInfo())
menu.removeFood(pizza)
print(menu.printInfo())
menu.addFood(Food("Sale",7,"eeeee"))
menu.printInfo()
print(menu.getAveragePrice())