from flask import Flask, render_template, request

api=Flask("__name__")

utenti=[["Mario","pass1"],["Marco","password"],["Davide","p2"],["Paolo","pass"]]

@api.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@api.route('/index2', methods=['GET'])
def index2():
    nome= request.args.get("nome")
    password= request.args.get("password")
    for u in utenti:
        if u[0].lower() == nome.lower() and u[1].lower()==password.lower():
            return render_template('index2.html',nome=nome,password=password)
    return render_template('index3.html')


api.run(host="0.0.0.0", port=8085)