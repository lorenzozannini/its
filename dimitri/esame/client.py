import requests,json
import sys 

base_url = "https://127.0.0.1:8080"

def Login():
    username=input("Inserisci username: ")
    password=input("Inserisci password: ")
    return {"username":username,"password":password}

def DatiCasavendita():
    dati={}
    keys=[]
    print("Lasciare vuoto se non si desidera cercare case con quel attributo")
    dati["citta"]=input("Inserisci città dove si desire acquistare-> ")
    try:
        dati["min_p"]=float(input("Inserisci prezzo minimo-> "))
    except:
        pass
    try:
        dati["max_p"]=float(input("Inserisci prezzo massimo-> "))
    except:
        pass
    try:
        dati["piano"]=int(input("Inserisci piano-> "))
    except:
        pass
    try:
        dati["metri"]=float(input("Inserisci metri-> "))
    except:
        pass
    try:
        dati["vani"]=float(input("Inserisci vani->"))
    except:
        pass
    dati["stato"]=input("Inserisci stato(LIBERO,OCCUPATO)-> ")
    
    for k,v in dati.items():
         if v == "":
              keys.append(k)
    for k in keys:
        dati.pop(k)
    return dati
              
def DatiCasaAffitto():
    dati={}
    keys=[]
    print("Lasciare vuoto se non si desidera cercare case con quel attributo")
    dati["citta"]=input("Inserisci città dove si desire acquistare-> ")
    try:
        dati["min_p"]=float(input("Inserisci prezzo minimo-> "))
    except:
        pass
    try:
        dati["max_p"]=float(input("Inserisci prezzo massimo-> "))
    except:
        pass
    bagno=input("Desideri il bagno personale(inserisci T o F)?-> ")
    if bagno=="T":
        dati["bagno_personale"]=True
    elif bagno=="F":
        dati["bagno_personale"]=False
    dati["tipo_affitto"]=input("Inserisci tipo di affitto(PARZIALE,TOTALE)-> ")
    
    for k,v in dati.items():
         if v == "":
              keys.append(k)
    for k in keys:
        dati.pop(k)
    return dati

while True:
    print("\nOperazioni disponibili:")
    print("1. Login")
    print("2. Esci")

    try:
        Oper = int(input("Cosa vuoi fare? "))
    except ValueError:
        print("Inserisci un numero valido!")
        continue

    if Oper==1:
        api_url = base_url + "/login"
        jsonDataRequest = Login()
        response = requests.post(api_url,json=jsonDataRequest, verify=False)
        print(response.json())

        if response.json()["login"]==True:
            
            username=jsonDataRequest["username"]
            password=jsonDataRequest["password"]
            filiale=response.json["filiale"]
            jsonDatiLogin={"username":username,"password":password,"filiale":filiale}
            
            while True:
                print("Cosa vuoi fare?\n1) Cerca una casa in vendita\n2) Cerca una casa in affitto\n3)Vendi casa\n4)Affitta casa,\n5)Affitta casa,\n6)Esci")
                n = int(input())
                if n == 1:
                    api_url = base_url + '/CercaCasaVendita'
                    jsonDataRequest = DatiCasavendita()
                    request= requests.post(api_url,json={"login":jsonDatiLogin,"dati":jsonDataRequest} , verify=False ) 
                    print(request.json())       
                elif n == 2:
                    api_url = base_url + '/CercaCasaAffitto'
                    jsonDataRequest= DatiCasaAffitto()
                    request= requests.post(api_url,json={"login":jsonDatiLogin,"dati":jsonDataRequest} , verify=False )
                    print(request.json())
                elif n == 3:
                    api_url = base_url + '/VendiCasa'
                    catastale= input("Inserisci catastale da acquistare-> ")
                    request= requests.post(api_url,json={"login":jsonDatiLogin,"catastale":catastale} , verify=False )
                    print(request.json())
                elif n == 4:
                    api_url = base_url + '/AffittaCasa'
                    catastale= input("Inserisci catastale da affittare-> ")
                    data=input("Inserisci data-> ")
                    request= requests.post(api_url,json={"login":jsonDatiLogin,"catastale":catastale,"data":data} , verify=False )
                    print(request.json())
                elif n==5:
                    api_url = base_url + '/CaseVendute'
                    datai=input("Inserisci data inizio-> ")
                    dataf=input("Inserisci data fine-> ")
                    request= requests.post(api_url,json={"data_inizio":datai,"data_fine":dataf} , verify=False )
                    print(request.json())
                elif n == 6:
                    sys.exit()