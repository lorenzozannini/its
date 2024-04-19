#6.1
persona={"Nome":"Lorenzo","Cognome":"Zannini","Età":19,"Città":"Roma"}
print(persona)

#6.2
numeri_p={"Lorenzo":5,"Davide":7,"Marco":89,"Sandro":451,"Francesco":10}
print(numeri_p)

#6.3
glossario={"Print":"Stampa","Float":"Numero decimale","Int":"Numero intero","Str":"Stringa"}
for i in glossario:
    print(i,":",glossario[i])

#6.7
persona1=persona
persona2={"Nome":"Mario","Cognome":"Rossi","Età":35,"Città":"Milano"}
persona3={"Nome":"Paolo","Cognome":"Bianchi","Età":75,"Città":"Napoli"}
persone=[persona1,persona2,persona3]
for i in persone:
    print(i)

#6.8
animale1={"Specie":"gatto","Proprietario":"Paolo"}
animale2={"Specie":"cane","Proprietario":"Marco"}
animale3={"Specie":"coniglio","Proprietario":"Davide"}
animali=[animale1,animale2,animale3]
for i in animali:
    print(i)

#6.9
favorite_places={"Mario":"Roma, Napoli, Venezia","Marco":"Madrid, Parigi, Monaco","Maria":"Ibiza, Corfù, Berlino"}
for i in favorite_places:
    print(i,":",favorite_places[i])

#6.10
numeri_p1=numeri_p={"Lorenzo":"5,25","Davide":"7,41","Marco":"89,631","Sandro":"451,414","Francesco":"10,30"}
for i in numeri_p1:
    print(i,":",numeri_p1[i])
    