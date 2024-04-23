import random

def stampal(l):
    for i in l:
        print(i) 

#4.1
pizze=["margherita","diavola","crostino"]
stampal(pizze)
for i in pizze:
    print("Mi piace la piza",i)
print("I like ",pizze[0])
print("My favourite pizza is ",pizze[1])
print("I hate ",pizze[2])

#4.2
animals=["dog","cat","bunny"]
stampal(animals)
print("I like ",animals[0])
print("My favourite pets is ",animals[1])
print("I hate ",animals[2])
print("They are all pets")

#4.3
for i in range(1,21):
    print(i)

#4.4
numbers=[]
for i in range(1,1000000):
    numbers.append(i)
stampal(numbers)

#4.5
print(max(numbers))
print(min(numbers))
print(sum(numbers))

#4.6
n1_20=[]
for i in range(1,21):
    n1_20.append(i)
stampal(n1_20)

#4.7
n3_30=[]
for i in range(3,31,3):
    n3_30.append(i)
stampal(n3_30)

#4.8
for i in range(1,11):
    print(i**3)

#4.9
cubes=[i**3 for i in range(1,11)]
print(cubes)

#4.11
friend_pizzas=pizze.copy()
pizze.append("boscaiola")
friend_pizzas.append("funghi")
for i in pizze:
    print("My favourite pizza are",i)
for i in friend_pizzas:
    print("My friend's favourite pizza are",i)

#5.1
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
pet="dog"
print(pet=="dog")
print(pet=="cat")
food="pizza"
print(food=="pizza")
print(food=="pasta")
drink="water"
print(drink=="water")
print(drink=="wine")
hobby="play videogames"
print(hobby=="play videogames")
print(hobby=="watch tv")

#5.2
color=["green","yellow","red"]
alien_color=random.choice(color)
if alien_color=="green":
    print("the player just earned 5 points.")

#5.4
if alien_color=="green":
    print("the player just earned 5 points.")
else:
    print("the player just earned 10 points.")
if alien_color=="green":
    print("the player just earned 5 points.")
elif alien_color !="green":
    print("the player just earned 10 points.")

#5.5
print("alien color is ",alien_color)
if alien_color=="green":
    print("the player just earned 5 points.")
elif alien_color =="yellow":
    print("the player just earned 10 points.")
else:
    print("the player just earned 15 points.")

#5.6
age=random.randint(0,100)
print("age=",age)
if age<2:
    print("the person is a baby")
if age>=2 and age<4:
    print("the person is a toddler")
if age>=4 and age<13:
    print("the person is a kid")
if age>=13 and age<20:
    print("the person is a teenager")
if age>=20 and age<65:
    print("the person is a adult")
if age> 65:
    print("the person is a elder")

#5.7
a=input("Inserisci frutto->")
favorite_fruits=["apples","banana","cherry"]
if a in favorite_fruits:
    print("You really like",a)

#5.8
usernames=["user","admin","pippo","mario","pluto"]
for i in usernames:
    if i=="admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello",i,", thank you for logging in again")

#5.10
current_users=["uSer","admIn","pippo","mario","pluto"]
current_users1=[]
new_users=["uSEr","aDmin","davide","silvio","matteo"]
for k in current_users:
    current_users1.append(k.lower())
for i in new_users:
    if i.lower() in current_users1:
        print("Username already in use: Enter a new usernamer")
    else:
         print("the username is available")

#5.11
numbers=[]
for i in range(1,10):
    numbers.append(i)
for i in numbers:
    if i>3:
        print(i,"th")
    elif i==1:
        print(i,"st")
    elif i==2:
        print(i,"nd")
    elif i==3:
        print(i,"rd")
