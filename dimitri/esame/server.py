from flask import Flask, json, request, render_template
import random
import os
import dbclient as db
import sys

api = Flask(__name__)

mydb = db.connect()

if mydb is None:
    print("Errore connessione al DB")
    sys.exit()

    
@api.route('/CercaCasaVendita', methods=['POST'])
def cercaCasaVendita():
    username=request.json["login"]["username"]
    password=request.json["login"]["password"]
    filiale=request.json["login"]["filiale"]
    if Login(username,password)==True:
        dati=request.json["dati"]
        dizf={}
        diznf={}
        query="SELECT * FROM case_in_vendita where"
        for k,v in dati.items():
            if k == "min_p":
                query+=f" prezzo > '{v}' AND"
            elif k=="max_p":
                query+=f" prezzo < '{v}' AND"
            else:
                query+=f" {k} = '{v}' AND"
        query=query[:-3]

        if db.read_in_db(mydb,query)>0:
            for i in range(1,db.read_in_db(mydb,query)):
                riga=db.read_next_row(mydb)[1]
                if riga[7]==filiale:
                    dizf[riga[0]]=riga[1:] 
                else:
                    diznf[riga[0]]=riga[1:]
            jsonResp = {"Esito":"200", "Case disponibili in questa filiale": dizf,"Case disponibili in un altra filiale": diznf}
            return json.dumps(jsonResp)
        elif db.read_in_db(mydb,query)==0:
            jsonResp = {"Esito":"200", "Msg":"Nessuna casa disponibile secondo questa ricerca"}
            return json.dumps(jsonResp)
        elif db.read_in_db(mydb,query)==-1:
            jsonResp = {"Esito":"400", "Msg":"Errore nella ricerca"}
            return json.dumps(jsonResp)
    else:
        jsonResp = {"Esito":"400", "Msg":"diritti negati"}
        return json.dumps(jsonResp)

@api.route('/CercaCasaAffitto', methods=['POST'])
def cercaCasaAffitto():
    username=request.json["login"]["username"]
    password=request.json["login"]["password"]
    filiale=request.json["login"]["filiale"]
    if Login(username,password)==True:
        dati=request.json["dati"]
        dizf={}
        diznf={}
        query="SELECT * FROM case_in_affitto where"
        for k,v in dati.items():
            if k == "min_p":
                query+=f" prezzo > '{v}' AND"
            elif k=="max_p":
                query+=f" prezzo < '{v}' AND"
            else:
                query+=f" {k} = '{v}' AND"
        query=query[:-3]

        if db.read_in_db(mydb,query)>0:
            for i in range(1,db.read_in_db(mydb,query)):
                riga=db.read_next_row(mydb)[1]
                if riga[7]==filiale:
                    dizf[riga[0]]=riga[1:] 
                else:
                    diznf[riga[0]]=riga[1:]
            jsonResp = {"Esito":"200", "Case disponibili in questa filiale": dizf,"Case disponibili in un altra filiale": diznf}
            return json.dumps(jsonResp)
        elif db.read_in_db(mydb,query)==0:
            jsonResp = {"Esito":"200", "Msg":"Nessuna casa disponibile secondo questa ricerca"}
            return json.dumps(jsonResp)
        elif db.read_in_db(mydb,query)==-1:
            jsonResp = {"Esito":"400", "Msg":"Errore nella ricerca"}
            return json.dumps(jsonResp)
    else:
        jsonResp = {"Esito":"400", "Msg":"diritti negati"}
        return json.dumps(jsonResp)
    
@api.route('/VendiCasa', methods=['POST'])
def VendiCasa():
    username=request.json["login"]["username"]
    password=request.json["login"]["password"]
    filiale=request.json["login"]["filiale"]
    if Login(username,password)==True:
        catastale=request.json["catastale"]
        data=request.json["data"]
        query=f"select stato,filiale_proponente,prezzo from case_in_vendita where catastale='{catastale}'"
        if db.read_in_db(mydb,query)==1:
            riga=db.read_next_row(mydb)[1]
            if riga[0]=="LIBERO":
                query=f"insert into vendite_case values('{catastale}',{data},'{filiale}','{riga[1]}',{riga[2]})"
                if db.write_in_db(mydb,query)==0:
                    query=f"update case_in_vendita set stato='OCCUPATO' where catastale='{catastale}'"
                    db.write_in_db(mydb,query)
                    jsonResp = {"Esito":"200", "Msg":"Casa acquistata"}
                    return json.dumps(jsonResp)
                elif db.write_in_db(mydb,query)==-1:
                    jsonResp = {"Esito":"400", "Msg":"Errore"}
                    return json.dumps(jsonResp)
            else:
                jsonResp = {"Esito":"200", "Msg":"Casa già acquistata"}
                return json.dumps(jsonResp)

@api.route('/CaseVendute', methods=['POST'])
def CaseVendute():
    datai=request.json["data_inizio"]
    dataf=request.json["data_fine"]
    query=f"select v.filiale_venditrice, count(*) as Numero_case_vendute, from vendite_case where data_vendita between {datai} and {dataf} group by (v.filiale_venditrice)"
    


@api.route('/login',methods=['POST'])
def GestisciLogin():
    utente=request.json  
    sQuery=f"select * from utenti where username='{utente['username']}' and password='{utente['password']}'"
    if db.read_in_db(mydb,sQuery)==1:
        jsonResp={"Esito":"200", "Msg":"login effettuato correttamente","login":True,"filiale":db.read_next_row(mydb)[1][2]}
        return json.dumps(jsonResp)
    else:
        jsonResp = {"Esito":"402", "Msg":"username o password errati", "login":False}
        return json.dumps(jsonResp)

def Login(utente,password):
    sQuery=f"select * from utenti where username='{utente}'and password='{password}'"
    if db.read_in_db(mydb,sQuery)>0: 
        return True
    else:
        return False
    

api.run(host="127.0.0.1", port=8080,ssl_context='adhoc')