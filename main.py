from flask import Flask, render_template,redirect,url_for,request
import os
import pandas as pd
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('NewInvoice.html')
@app.route('/success',methods=['POST','GET'])
def success():
    if request.method=='POST':
        ino=request.form['ino']
        company=request.form['company']
        dict1 = {'no': [ino], 'company': [company]}
        df = pd.read_csv(r"bills.csv", index_col=0)
        ind = df.tail(1).index
        df.loc[ind[0] + 1] = [ino, company]
        df.to_csv('bills.csv')
        return 'Success'

if __name__=='__main__':
    app.run(debug=True)


