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
	print("hello world", file=sys.stderr)
	return render_template("index.html");

@app.route('/dashboard')
def dashboard():
	print("In Dashboard",  file=sys.stderr)
	print(youremail,  file=sys.stderr)
	return render_template("dashboard.html", email=youremail);

@app.route('/bad', methods=['POST'])
def secret_bad_thing():
	print("here",  file=sys.stderr)
	global youremail
	youremail = request.form["youremail"];
	print(youremail, file=sys.stderr)
	print("anna was here",  file=sys.stderr)
	return redirect('/dashboard')

#dashboard landing page   
@app.route('/dashboard', methods = ['POST'])
def dashboard():
	#emailAddress = request.form["emailAddress"]
	return render_template("dashboard.html")
	
#page for creating profile
@app.route('/createProfile')
def createProfilePage():
	return render_template("createProfile.html")

#creating profile form action 
@app.route('/profileUpdate', methods=['POST'])
def createProfile():
	#id = id_generator()
	emailAddress = request.form["emailAddress"]
 	#route = "/" + emailAddress
 	#result = firebase.get(route, None)
#  	while result != None:
#  		id = id_generator()
#  		route = "/" + id
#  		result = firebase.get(route, None)
 	
 
 	type = request.form["type"]	
 	name = request.form["name"]
 	age = request.form["age"]
	city = request.form["city"]
	country = request.form["country"]
	experience = request.form["experienceLevel"]
	interests = request.form["interests"]
	bio = request.form["bio"]
	
	
	route = "/" + emailAddress
	firebase.put(route,"Type", type)
 	firebase.put(route, "Name", name)
 	firebase.put(route, "Age", age)
 	firebase.put(route, "City", city)
 	firebase.put(route, "Country", country)
 	firebase.put(route, "Experience", experience)
 	firebase.put(route, "Interests", interests)
 	firebase.put(route, "Bio", bio)
 	
 	return redirect('/ready');

@app.route('/viewProfile', methods=['GET'])
def viewProfile():
	return_list = []
	results = firebase.get('/', None)
	for id in results.key():
		if id == emailAddress:
			type = results[id]["Type"]	
			name = results[id]["Name"]
			age = results[id]["Age"]
			city = results[id]["City"]
			country = results[id]["Country"]
			experience = results[id]["Experience"]
			interests = results[id]["Interests"]
			bio = results[id]["Bio"]
			
			return_list.append(type)
			return_list.append(name)
			return_list.append(age)
			return_list.append(city)
			return_list.append(country)
			return_list.append(experience)
			return_list.append(interests)
			return_list.append(bio)
			
			return render_template("viewProfile.html", return_list = return_list)
			
		
			
@app.route('/browse', methods=['GET'])
def browse():
	return_list = []
	results = firebase.get('/', None)
	count = 1
	for id in results.keys():
		if (results[id]["Type"] == "mentor"):
			local_list = []
			local_list.append(count)
			local_list.append(results[id]["Name"])
			local_list.append(results[id]["Age"])
			local_list.append(results[id]["City"])
			local_list.append(results[id]["Country"])
			local_list.append(results[id]["Experience"])
			local_list.append(results[id]["Interests"])
			local_list.append(results[id]["Bio"])
			return_list.append(local_list)
			count = count + 1
		
	return render_template("browse.html", return_list=return_list)
		
@app.route('/filter', methods = ["GET", "POST"])
def filter():
	
	item_choice = request.form["interests"]
	return_list = []
	results = firebase.get('/', None)
	count = 1
	for id in results.keys():
		if (results[id]["Type"] == "mentor" and results[id]["Interests"] == item_choice):
			local_list = []
			local_list.append(count)
			local_list.append(results[id]["Name"])
			local_list.append(results[id]["Age"])
			local_list.append(results[id]["City"])
			local_list.append(results[id]["Country"])
			local_list.append(results[id]["Experience"])
			local_list.append(results[id]["Interests"])
			local_list.append(results[id]["Bio"])
			return_list.append(local_list)
			count = count + 1
		
	return render_template("filteredBrowse.html", return_list=return_list)
# 	animal_choice = request.form["animal"]
# 	depth_choice = request.form["depth"]
# 	recovered_choice = request.form["isRecovered"]
# 	material_choice = request.form["material"]
	

# @app.route('/add', methods=['POST'])
# def add():
# 	id = id_generator()
# 	route = "/" + id
# 	result = firebase.get(route, None)
# 	while result != None:
# 		id = id_generator()
# 		route = "/" + id
# 		result = firebase.get(route, None)
# request.form[nameofinputelement]
# 	item = request.form["item"]
# 	animal = request.form["animal"]
# 	depth = request.form["depth"]
# 	recovered = request.form["isRecovered"]
# 	material = request.form["material"]
# 	lat = request.form["lat"]
# 	lon = request.form["lon"]
# 	photo = request.form["photo"]
# 	comment = request.form["comment"]

# 	print comment

# 	route = "/" + id
# 	firebase.put(route, "Item", item)
# 	firebase.put(route, "Animals", animal)
# 	firebase.put(route, "Depth", depth)
# 	firebase.put(route, "Recovered", recovered)
# 	firebase.put(route, "Material", material)
# 	firebase.put(route, "Lat", lat)
# 	firebase.put(route, "Lon", lon)
# 	firebase.put(route, "Photo", photo)
# 	firebase.put(route,"Comment", comment)

# 	return redirect('/thankyou');

# @app.route('/display', methods=['GET', 'POST'])
# def display():
	
# 	item_choice = request.form["item"]
# 	animal_choice = request.form["animal"]
# 	depth_choice = request.form["depth"]
# 	recovered_choice = request.form["isRecovered"]
# 	material_choice = request.form["material"]

# 	return_list = []
# 	results = firebase.get('/', None)

# 	count = 1
# 	for id in results.keys():

# 		if (filter_recovered(recovered_choice, results[id]["Recovered"]) and filter_material(material_choice, results[id]["Material"]) and filter_animal(animal_choice, results[id]["Animals"]) and results[id]["Item"] == item_choice and filter_depth(depth_choice, results[id]["Depth"])):
# 			local_list = []
# 			local_list.append(count)
# 			local_list.append(results[id]["Item"])
# 			local_list.append(results[id]["Animals"])
# 			local_list.append(results[id]["Recovered"])
# 			local_list.append(results[id]["Depth"])
# 			local_list.append(results[id]["Lat"])
# 			local_list.append(results[id]["Lon"])
# 			local_list.append(results[id]["Photo"])
# 			if results[id]["Comment"]:
# 				local_list.append(results[id]["Comment"])

# 			return_list.append(local_list)
# 			count = count + 1
# 	print len(return_list)
# 	if len(return_list) == 0:
# 		return render_template("display_entriesFail.html")
# 	else:
# 		return render_template("display_entries.html", return_list=return_list)


if __name__ == '__main__':
    app.run()
