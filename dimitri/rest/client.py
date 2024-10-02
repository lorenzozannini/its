import requests,json,sys

base_url="http://127.0.0.1:8080"

def GetDatiCittadino():
    nome = input("Inserisci nome: ")
    cognome = input("Inserisci cognome: ")
    dataN = input("Inserisci data di nascita: ")
    codF = input("Inserisci codice fiscale: ")
    datiCittadino = {codF:{"nome":nome, "cognome": cognome, "data nascita":dataN, "codice fiscale":codF}}
    return datiCittadino

def GetCodiceFiscale():
    cod=input("Inserisci codice fiscale: ")
    return cod

def GetUpdate():
    nome = input("Inserisci nome: ")
    cognome = input("Inserisci cognome: ")
    dataN = input("Inserisci data di nascita: ")
    codF = input("Inserisci codice fiscale: ")
    datiCittadino = {"nome":nome, "cognome": cognome, "data nascita":dataN,"codice fiscale":codF}
    return codF,datiCittadino

while True:
    print("\nOperazioni disponibili:")
    print("1. Inserisci cittadino")
    print("2. Richiedi cittadino")
    print("3. Modifica cittadino")
    print("4. Elimina cittadino")
    print("5. Login cittadino")
    print("6. Esci")

    try:
        sOper = int(input("Cosa vuoi fare? "))
    except ValueError:
        print("Inserisci un numero valido!")
        continue
    if sOper==1:
        api_url = base_url + "/add_cittadino"
        jsonDataRequest = GetDatiCittadino()
        response = requests.post(api_url,json=jsonDataRequest)
        data1 = response.json()
        print(data1)
    elif sOper==2:
        api_url=base_url+"/read_cittadino"
        jsonDataRequest = GetCodiceFiscale()
        response = requests.post(api_url,json=jsonDataRequest)
        print(response.json())
    elif sOper==3:
        api_url=base_url+"/update_cittadino"
        jsonDataRequest = GetUpdate()
        response = requests.post(api_url,json=jsonDataRequest)
        print(response.json())
    elif sOper==4:
        api_url=base_url+"/delete_cittadino"
        jsonDataRequest = GetCodiceFiscale()
        response = requests.post(api_url,json=jsonDataRequest)
        print(response.json())
    elif sOper==5:
        api_url=base_url+"/login_cittadino"
        jsonDataRequest = GetUpdate()
        response = requests.post(api_url,json=jsonDataRequest)
        print(response.json())
    elif sOper==6:
        sys.exit()