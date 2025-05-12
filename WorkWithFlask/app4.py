from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

Data=[]



@app.get('/')
def get():
	for x in Data:
		if x['Data'] == name:
			return x
	return {'Data':None}

@app.post('/Name/<string:name>')
def add_user(name):
	Tem = {'Data':name}
	Data.append(Tem)
	return redirect('/')

@app.route('/delete/<string:name>')
def delete_user(name):
	for ind,x in enumerate(Data):
		if x['Data'] == name:
			Tem=Data.pop[name]
	return {'Note':"Deleted"}
   

if __name__ == '__main__':
    app.run(debug=True)
