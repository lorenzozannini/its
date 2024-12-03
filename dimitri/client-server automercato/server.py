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


@api.route('/ControlloFiliale', methods=['POST'])
def cercaFiliale():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)

    filiale = request.json["filiale"]

    query = f"select * from automobile a,motociclette m where a.filiale = '{filiale}' OR m.filiale = '{filiale}'"
    
    if db.read_in_db(mydb, query) > 0:
        return json.dumps({"Risposta" : 1})

    return json.dumps({"Risposta" : -1})

    
@api.route('/CercaAutomobile', methods=['POST'])
def cercaAutomobile():
	content_type = request.headers.get('Content-Type')
	print("Ricevuta chiamata " + content_type)
	prezzo=request.json["prezzo"]
	modello=request.json["modello"]
	kilometraggio=request.json["kilometraggio"]
	filiale=request.json["filiale"]
	query=f"select * from automobile where prezzo='{prezzo}' AND modello='{modello}' AND kilometraggio='{kilometraggio}'"
	diz={}
	if db.read_in_db(mydb,query)>0:
		for i in range(1,db.read_in_db(mydb,query)):
			if db.read_next_row[i][5] == filiale:
				diz[db.read_next_row[i][0]]="Automobile disponibile in questa filiale"
			else:
				diz[db.read_next_row[i][0]]="Automobile disponibile nella filiale numero"+db.read_next_row[i][5]
	return json.dumps({"Automobili disponibili": diz})

@api.route('/CercaMotocicletta', methods=['POST'])
def cercaMotocicletta():
	content_type = request.headers.get('Content-Type')
	print("Ricevuta chiamata " + content_type)
	prezzo=request.json["prezzo"]
	modello=request.json["modello"]
	kilometraggio=request.json["kilometraggio"]
	filiale=request.json["filiale"]
	query=f"select * from motocicletta where prezzo='{prezzo}' AND modello='{modello}' AND kilometraggio='{kilometraggio}'"
	diz={}
	if db.read_in_db(mydb,query)>0:
		for i in range(1,db.read_in_db(mydb,query)):
			if db.read_next_row[i][5] == filiale:
				diz[db.read_next_row[i][0]]="Motocicletta disponibile in questa filiale"
			else:
				diz[db.read_next_row[i][0]]="Motocicletta disponibile nella filiale numero"+db.read_next_row[i][5]
	return json.dumps({"Motociclette disponibili": diz})

api.run(host="127.0.0.1", port=8080,ssl_context='adhoc')