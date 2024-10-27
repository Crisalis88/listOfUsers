from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import csv

app = Flask(__name__)

users = []

@app.route('/')
@app.route('/registration')
def hello():
	return render_template('registration.html')


@app.route('/home')
def home():
	name = request.args.get('name', 'User')
	file = open('register.csv', 'a')
	writer = csv.writer(file)
	writer.writerow(name)
	file.close()
	return render_template('index.html')


@app.route('/users')
def allUsers():
	file = open('register.csv', 'r')
	reader = csv.reader(file)
	users = list(reader)
	file.close()
	return render_template('users.html', users = users)
















