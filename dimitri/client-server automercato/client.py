import requests,json
import sys 

base_url = "https://127.0.0.1:8080"
auth = False

a = True
while a:
    print("Da quale filiale stai accedendo?")
    filiale = input()
    fil_diz = {"filiale" : filiale}

    api_url = base_url + '/ControlloFiliale'
    risposta = requests.post(api_url, fil_diz, verify=False)

    if risposta.json()["Risposta"] == 1:
        a = False
    else:
        print("La filiale non esiste riprovare")
        

while True:
    
    if not auth:

        print("Cosa vuoi fare\n1) Cerca un automobile\n2) Cerca una motocicletta\n3)esci")
        n = input()
        
        if n == 1:
            api_url = base_url + '/CercaAutomobile'
            
            print("Mettere i parametri di ricerca\nprezzo(intero")
            rispsota_veicolo = input()
            
            print("Mettere il modello")
            rispsota_veicolo2 = input()

            print("Mettere il Kilometraggio")
            rispsota_veicolo3 = input()

            diz_risp_veicolo = {"prezzo" : rispsota_veicolo, "modello" : rispsota_veicolo2, "kilometraggio" : rispsota_veicolo3, "filiale": filiale}
            request_automobile = requests.post(api_url, diz_risp_veicolo, verify=False )
            print(request_automobile.json())

        elif n == 2:
            api_url = base_url + '/CercaMotocicletta'
            
            print("Mettere i parametri di ricerca\nprezzo(intero")
            rispsota_veicolo = input()
            
            print("Mettere il modello")
            rispsota_veicolo2 = input()

            print("Mettere il Kilometraggio")
            rispsota_veicolo3 = input()

            diz_risp_veicolo = {"prezzo" : rispsota_veicolo, "modello" : rispsota_veicolo2, "kilometraggio" : rispsota_veicolo3, "filiale": filiale}
            request_motocicletta = requests.post(api_url, diz_risp_veicolo, verify=False )
            print(request_motocicletta.json())

        elif n == 3:
            auth = True