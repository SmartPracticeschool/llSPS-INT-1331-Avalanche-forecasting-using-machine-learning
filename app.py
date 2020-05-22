# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask,render_template,request

import pickle
import numpy as np

model = pickle.load(open('Avalanche.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login',methods=['POST','get'])
def login():
    te = request.form['te']
    hu = request.form['hu']
    sd = request.form['sd']
    ws = request.form['ws']
    m = request.form['m']
    if(m == "march"):
        m1,m2,m3,m4,m5 = 0.,0.,0.,1.,0.
    if(m == "april"):
        m1,m2,m3,m4,m5 = 1.,0.,0.,0.,0.
    if(m == "june"):
        m1,m2,m3,m4,m5 = 0.,0.,1.,0.,0.
    if(m == "may"):
        m1,m2,m3,m4,m5 = 0.,0.,0.,0.,1.
    if(m == "febraury"):
        m1,m2,m3,m4,m5 = 0.,1.,0.,0.,0.
    total = [[m1,m2,m3,m4,m5,float(te),float(hu),rloat(sd),float(ws)]]
    print(total)
    y_pred = model.predict()
    
    print(y_pred)
    
    return render_template("index.html",showcase = y_pred)
    if __name__=='__main__':
        app.run(debug = True)
