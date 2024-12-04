from flask import Flask,render_template,request
import sys

api=Flask(__name__)

@api.route('/',methods=['GET'])
def index():
    return render_template('send.html')

api.run(host="0.0.0.0",port=8080)