def stampad(d):
    for i in d:
        print(i,":",d[i])

def stampal(l):
    for i in l:
        print(i)
#3.4
dinner_p=["Totti","De Rossi","Cristante"]
for i in dinner_p:
    print("Ciao",i,"ti andrebbe di venire a cena con me")

#3.5
print("")
print("Purtroppo",dinner_p[2],"non ha accettato l'invito al suo posto verra Messi")
dinner_p.pop(2)
dinner_p.append("Messi")
for i in dinner_p:
    print("Ciao",i,"ti andrebbe di venire a cena con me")


#3.6
print("")
print("Ho trovato un tavolo più grande inviterò altre 3 persone")
dinner_p.insert(0,"Pippo")
dinner_p.insert(2,"Pluto")
dinner_p.insert(5,"Paperino")
for i in dinner_p:
    print("Ciao",i,"ti andrebbe di venire a cena con me")

#3.7
print("")
print("Purtroppo non ho più spazio e riesco a invitare solo 2 persone")
while len(dinner_p)>2:
    print("Mi dispiace",dinner_p[-1],"non riesco più a invitarti")
    dinner_p.pop()
for i in dinner_p:
    print("Ciao",i,"sei ancora invitato")
dinner_p.remove(dinner_p[0])
dinner_p.remove(dinner_p[0])
print(dinner_p)

#3.8
locations=["Parigi","Amsterdam","Firenze","Sardegna","Grecia"]
print(locations)
print(sorted(locations))
print(locations)
print(sorted(locations)[::-1])
print(locations)
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)

#3.9
print(len(dinner_p))

#6.1
person={"Nome":"Lorenzo","Cognome":"Zannini","Età":19,"Città":"Roma"}
print(person)

#6.2
f_numbers={"Lorenzo":5,"Davide":7,"Marco":89,"Sandro":451,"Francesco":10}
print(f_numbers)

#6.3
glossary={"Print":"stampad","Float":"Numero decimale","Int":"Numero intero","Str":"Stringa"}
stampad(glossary)

#6.7
person1=person
person2={"Nome":"Mario","Cognome":"Rossi","Età":35,"Città":"Milano"}
person3={"Nome":"Paolo","Cognome":"Bianchi","Età":75,"Città":"Napoli"}
people=[person1,person2,person3]
stampal(people)

#6.8
pet1={"Specie":"gatto","Proprietario":"Paolo"}
pet2={"Specie":"cane","Proprietario":"Marco"}
pet3={"Specie":"coniglio","Proprietario":"Davide"}
pets=[pet1,pet2,pet3]
stampal(pets)

#6.9
favorite_places={"Mario":"Roma, Napoli, Venezia","Marco":"Madrid, Parigi, Monaco","Maria":"Ibiza, Corfù, Berlino"}
stampad(favorite_places)

#6.10
f_numbers1=f_numbers={"Lorenzo":"5,25","Davide":"7,41","Marco":"89,631","Sandro":"451,414","Francesco":"10,30"}
stampad(f_numbers1)
#6.11
cities={"Roma":"Si trova in Italia, ha una popolazione di 2.755.309 abitanti ed è la capitale italiana","Parigi":"Si trova in Francia, ha una popolazione di 2.229.095 abitanti ed ospita disneyland paris","Londra":"Si trova nel Regno Unito, ha una popolazione di 8.799.800 e come valuta vengono usate le sterline "}
stampad(cities)
