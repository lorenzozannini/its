class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

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
for i in people:
    if i.age<min:
        min=i.age
print(min)