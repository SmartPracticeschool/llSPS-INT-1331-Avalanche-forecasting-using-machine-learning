# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from flask import Flask,render_template,request
import pickle
import numpy as np
model = pickle.load(open('Avalanche.pkl','rb'))
app1 = Flask(__name__)
@app1.route('/')
def home():
    return render_template("index.html")
@app1.route('/login',methods=['POST','GET'])

def login():
 te = float(request.form['te'])
 hu = flaot(request.form['hu'])
 sd = float(request.form['sd'])
 ws = floaat(request.form['ws'])
 m = request.form['m']
 if(m == "march"):
    m1,m2,m3,m4,m5 = 0.,0.,0.,1.,0.
 elif(m == "april"):
    m1,m2,m3,m4,m5 = 1.,0.,0.,0.,0.
 elif(m == "june"):
    m1,m2,m3,m4,m5 = 0.,0.,1.,0.,0.
 elif(m == "may"):
    m1,m2,m3,m4,m5 = 0.,0.,0.,0.,1.
 elif(m == "febraury"):
    m1,m2,m3,m4,m5 = 0.,1.,0.,0.,0.
 total = [[m1,m2,m3,m4,m5,int(te),int(hu),int(sd),int(ws)]]
 print(total)
 y_pred = model.predict((total))
 print(y_pred)
 return render_template("index.html",showcase = str(y_pred))
if __name__ == '__main__':
      app1.run(debug = True)