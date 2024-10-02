from flask import Flask,json,request
from myjson import *

api=Flask(__name__)
path="anagrafe.json"
cittadini=JsonDeserialize(path)

@api.route('/add_cittadino',methods=['POST'])
def GestisciAddCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        jsonReq = request.json
        for c in cittadini.keys():
            if list(jsonReq.keys())[0] ==c:
                jsonResp = {"Esito":"200", "Msg":"cittadino gia presente"}
                return json.dumps(jsonResp)
        cittadini.update(jsonReq)
        JsonSerialize(cittadini,path)
        jsonResp = {"Esito":"200", "Msg":"cittadino aggiunto"}
        return json.dumps(jsonResp)
    else:
        return 'Content-Type not supported!'

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
            JsonSerialize(cittadini,path)
            return json.dumps(jsonResp)
    jsonResp = {"Esito":"200", "Msg":"cittadino non presente"}
    return json.dumps(jsonResp)

@api.route('/delete_cittadino',methods=['POST'])
def GestisciDeleteCittadino():
    cod=request.json
    for c in cittadini:
        if cod==c:
            del cittadini[cod]
            jsonResp = {"Esito":"200", "Msg":"cittadino rimosso"}
            JsonSerialize(cittadini,path)
            return json.dumps(jsonResp)
    jsonResp = {"Esito":"200", "Msg":"cittadino non presente"}
    return json.dumps(jsonResp)

@api.route('/login_cittadino',methods=['POST'])
def GestisciLoginCittadino():
    cod,info=request.json
    for c,d in cittadini.items():
        if cod==c:
            if info["nome"]==d["nome"]:
                if info["cognome"]==d["cognome"]:
                    if info["data nascita"]==d["data nascita"]:
                        if info["codice fiscale"]==d["codice fiscale"]:
                            return {"Esito":"200", "Msg":"cittadino autorizzato"}
                        else:
                            jsonResp = {"Esito":"200", "Msg":"codice fiscale non corretto"}
                            return json.dumps(jsonResp)
                    else:
                        jsonResp = {"Esito":"200", "Msg":"data di nascita non corretta"}
                        return json.dumps(jsonResp)
                else:
                    jsonResp = {"Esito":"200", "Msg":"cognome non corretto"}
                    return json.dumps(jsonResp)
            else:
                jsonResp = {"Esito":"200", "Msg":"nome non corretto"}
                return json.dumps(jsonResp)
    jsonResp = {"Esito":"200", "Msg":"cittadino non presente"}
    return json.dumps(jsonResp)

api.run(host="127.0.0.1", port=8080)

