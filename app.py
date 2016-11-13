from xml.etree.ElementTree import fromstring
from firebase import firebase

from flask import Flask, render_template, request,json,jsonify, redirect
import urllib

import random
import string

import sys


app = Flask(__name__)
firebase = firebase.FirebaseApplication("https://ladyproblems-b9a2f.firebaseio.com/#-AIzaSyBUphDgfDUxvvSVWudfLnRMybVcPy_jT58",None)

def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

#home page
@app.route('/')
def hello_world():
	return render_template("landingPage.html");

@app.route('/landing')
def landing():
	return render_template("landingPage.html")

@app.route('/createProfile')
def create_profile():
	return render_template("createProfile.html");

@app.route('/dashboard')
def dashboard():
	return render_template("dashboard.html", email=youremail);

@app.route('/bad', methods=['POST'])
def secret_bad_thing():
	global youremail
	youremail = request.form["youremail"];
	global yourID
	yourID = request.form["yourID"];
	return redirect('/dashboard')

# #dashboard landing page   
# @app.route('/dashboard', methods = ['POST'])
# def dashboard():
# 	#emailAddress = request.form["emailAddress"]
# 	return render_template("dashboard.html")
	
#page for creating profile
@app.route('/createProfile')
def createProfilePage():
	return render_template("createProfile.html")

#creating profile form action 
@app.route('/profileUpdate', methods=['POST'])
def createProfile():
	id = id_generator()
	emailAddress = youremail
#  	route = "/" + emailAddress
#  	result = firebase.get(route, None)
#  	while result != None:
#  		id = id_generator()
#  		route = "/" + id
#  		result = firebase.get(route, None)
#  	
 
	role = request.form["role"]
	print (role)
	firstName = request.form["firstName"]
	print (firstName)
	lastName = request.form["lastName"]
	print (lastName)
	age = request.form["age"]
	print (age)	
	city = request.form["city"]
	print (city)
	country = request.form["country"]
	print (country)
	province = request.form["province"]
	print (province)
	interests = request.form["interests"]
	print (interests)
	bio = request.form["bio"]
	print (bio)
	
	
	route = "/" + yourID
	firebase.put(route,"email", youremail)
	firebase.put(route,"role", role)
	firebase.put(route, "firstName", firstName)
	firebase.put(route, "lastName", lastName)
	firebase.put(route, "age", age)
	firebase.put(route, "city", city)
	firebase.put(route, "country", country)
	firebase.put(route, "province", province)
	firebase.put(route, "interests", interests)
	firebase.put(route, "bio", bio)
 	
	return render_template('createProfile.html');

@app.route('/viewProfile', methods=['GET'])
def viewProfile():
	return_list = []
	results = firebase.get('/', None)
	for id in results.key():
		if id == emailAddress:
			role = results[id]["role"]	
			name = results[id]["name"]
			age = results[id]["age"]
			city = results[id]["city"]
			country = results[id]["country"]
			interests = results[id]["interests"]
			bio = results[id]["bio"]
			
			return_list.append(role)
			return_list.append(name)
			return_list.append(age)
			return_list.append(city)
			return_list.append(country)
			return_list.append(experience)
			return_list.append(interests)
			return_list.append(bio)
			
			return render_template("viewProfile.html", return_list = return_list)
			
@app.route('/searchMentors')
def browseForm():
	return render_template("browseForm.html");		
			
@app.route('/browse', methods=['GET'])
def browse():
	return_list = []
	results = firebase.get('/', None)
	count = 1
	for id in results.keys():
		if (results[id]["role"] == "mentor"):
			local_list = []
			local_list.append(count)
			local_list.append(results[id]["firstName"])
			local_list.append(results[id]["lastName"])
			local_list.append(results[id]["age"])
			local_list.append(results[id]["city"])
			local_list.append(results[id]["country"])
			local_list.append(results[id]["interests"])
			print(results[id]["interests"])
			local_list.append(results[id]["bio"])
			local_list.append(results[id]["email"])
			print (results[id]["email"])
			return_list.append(local_list)
			count = count + 1
		
	return render_template("browse.html", return_list=return_list)
		
@app.route('/filter', methods = ["GET", "POST"])
def filter():
	
	item_choice = request.form["interests"]
	city = request.form["city"]
	province = request.form["province"]
	country = request.form["country"]
	return_list = []
	results = firebase.get('/', None)
	count = 1
	for id in results.keys():
		if (results[id]["role"] == "mentor" and results[id]["interests"] == item_choice and results[id]["city"] == city and results[id]["province"] == province and results[id]["country"] == country):
			local_list = []
			local_list.append(count)
			local_list.append(results[id]["firstName"])
			local_list.append(results[id]["lastName"])
			local_list.append(results[id]["age"])
			local_list.append(results[id]["city"])
			local_list.append(results[id]["country"])
			local_list.append(results[id]["interests"])
			print(results[id]["interests"])
			local_list.append(results[id]["bio"])
			local_list.append(results[id]["email"])
			print (results[id]["email"])
			return_list.append(local_list)
			count = count + 1
	
	if len(return_list) == 0:
		return render_template("filteredBrowseFailed.html")	
	return render_template("filteredBrowse.html", return_list=return_list)



if __name__ == '__main__':
    app.run(debug=True)
