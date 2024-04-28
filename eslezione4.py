
from printing_functions import display_message,favorite_book,make_shirt 

#8.1
display_message()
#8.2

favorite_book("Alice in Wonderland")

#8.3
def make_shirt(size,text):
    print("size:",size,"text message",text)
make_shirt("large","I love pizza")

#8.4
def make_shirt(size,text):
    if size=="large":
        text="I love Python"
    print("size:",size,"text message:",text)
make_shirt("large","I like pasta")
make_shirt("medium","I like pasta")
make_shirt("small","I like videogames")

#8.5
def description_city(city):
    country="Italia"
    print(city,"is in",country)
description_city("Roma")
description_city("Milano")
description_city("Parigi")
#8.6
def city_country(city,country):
    print(city,",",country)
city_country("Roma","Italia")
city_country("Parigi","Francia")
city_country("Santiago","Chile")

#8.7
def make_album(name,title,song):
    d={}
    d["Name"]=name
    d["Title"]=title
    d["Song"]=song
    return d
print(make_album("pippo","sole",None))
print(make_album("mario","luna",17))

#8.8
while True:
    name=input("Inserisci nome artista-> ")
    title=input("Inserisci il titolo dell'album-> ")
    print(make_album(name,title,None))
    break

#8.9
def show_messages(l):
    for i in l:
        print(i)
messages=["Ciao","Come stai?","Mi piace la pizza"]
show_messages(messages)

#8.10
def send_messages(l):
    send_messages=[]
    for i in l:
        print(i)
        send_messages.append(i)
    return (send_messages)
sent_messages = send_messages(messages)
print(send_messages(messages))

#8.11
messages1=messages.copy()
print(send_messages(messages1))
print(messages)

#8.12
def sandwiches(*arg):
    for i in arg:
        print(i)
sandwiches("pane","formaggio","salame","insalata")
print("")
sandwiches("pane","hamburger","maionese")
print("")
sandwiches("pane","cotoletta")
print("")

#8.13
def build_profile(name,surmame,age,hair,weight):
    print(name,surmame,",age",age,",hair",hair,", weight",weight)
build_profile("mario","rossi",20,"brown",50)
build_profile("pippo","bianchi",50,"white",77)
build_profile("carlo","verdi",88,"grey",67)

#8.14
def cars(manufact,model,*arg):
    d={}
    d["Manufacturer"]=manufact
    d["Model name"]=model
    for i in range (0,len(arg),2):
        d[arg[i]]=arg[i+1]
    return d
print(cars("subaru","outback", "Color","blue","Tow_package",True))