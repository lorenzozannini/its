
def Serializza(l):
    list='['
    for n in l[0:-1]:
        list+=f"'{n}',"
    list+=f"'{l[-1]}'"+']'
    return str(list)

def Deserializza(l):
    list=l.split(",")
    list[0]=list[0].replace("[","")
    list[-1]=list[-1].replace("]","")
    for i in range(len(list)):
        list[i]=list[i].replace("'","")
    return list


mylist_1="['mario','gino','lucrezia']"
mylist_2=['mario','gino','lucrezia']
out=Serializza(mylist_2)
if out==mylist_1:
    print("Procedura di serializzazione costruita correttamente")
else:
    print("Procedura di serializzazione NON costruita correttamente")

out2=Deserializza(mylist_1)
if out2==mylist_2:
    print("Procedura di deserializzazione costruita correttamente")
else:
    print("Procedura di deserializzazione NON costruita correttamente")