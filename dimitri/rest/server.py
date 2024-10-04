from flask import Flask,json,request
from myjson import *

api=Flask(__name__)
pAnagrafe="anagrafe.json"
pUtenti="utenti.json"
cittadini=JsonDeserialize(pAnagrafe)
utenti=JsonDeserialize(pUtenti)

@api.route('/add_cittadino',methods=['POST'])
def GestisciAddCittadino():
    jsonReq = request.json
    for c in cittadini.keys():
        if list(jsonReq.keys())[0] ==c:
            jsonResp = {"Esito":"200", "Msg":"cittadino gia presente"}
            return json.dumps(jsonResp)
    cittadini.update(jsonReq)
    JsonSerialize(cittadini,pAnagrafe)
    jsonResp = {"Esito":"200", "Msg":"cittadino aggiunto"}
    return json.dumps(jsonResp)

@api.route('/read_cittadino',methods=['POST'])
def GestisciReadCittadino():
    cod=request.json
    for c in cittadini:
        if cod==c:
            jsonResp = {"Esito":"200", "Msg":"ok","Dati cittadino":cittadini[c]}
            return json.dumps(jsonResp)
    jsonResp = {"Esito":"200", "Msg":"cittadino non presente"}
    return json.dumps(jsonResp)

@api.route('/update_cittadino',methods=['POST'])
def GestisciUpdateCittadino():
    cod,info=request.json
    for c in cittadini.keys():
        if cod ==c:
            cittadini[c]=info
            jsonResp = {"Esito":"200", "Msg":"dati cittadino aggiornati"}
            JsonSerialize(cittadini,pAnagrafe)
    jsonResp = {"Esito":"200", "Msg":"cittadino non presente"}
    return json.dumps(jsonResp)

@api.route('/delete_cittadino',methods=['POST'])
def GestisciDeleteCittadino():
    cod=request.json
    for c in cittadini:
        if cod==c:
            del cittadini[cod]
            jsonResp = {"Esito":"200", "Msg":"cittadino rimosso"}
            JsonSerialize(cittadini,pAnagrafe)
            return json.dumps(jsonResp)
    jsonResp = {"Esito":"200", "Msg":"cittadino non presente"}
    return json.dumps(jsonResp)

@api.route('/login',methods=['POST'])
def GestisciLogin():
    utente=request.json  
    for u in utenti:
        if list(utente.keys())[0]==u:
            if list(utente.values())[0]==utenti[u]:
                jsonResp = {"Esito":"200", "Msg":"login eseguito con successo", "login":True}
                return json.dumps(jsonResp)
            else:
                jsonResp = {"Esito":"400", "Msg":"username o password errati", "login":False}
                return json.dumps(jsonResp)
    jsonResp = {"Esito":"400", "Msg":"username o password errati", "login":False}
    return json.dumps(jsonResp)

def Login(utente,password):
    if utente in utenti:
        if password==utenti[utente]:
            return True
        else:
            return False
    else:
        return False
       
           

api.run(host="127.0.0.1", port=8080,ssl_context='adhoc')