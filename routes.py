from flask import render_template, request, redirect, flash
from sqlalchemy.sql import text
from app import app
from db import db
from restaurants import search_restaurants, delete_restaurant, get_all_restaurants, add_restaurant
from reviews import get_reviews, add_review
import users

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/new")
def new():
    restaurants = get_all_restaurants()
    return render_template("new.html", restaurants=restaurants)

@app.route("/restaurants")
def restaurants():
    restaurants = get_all_restaurants()
    return render_template("restaurants.html", count=len(restaurants), restaurants=restaurants) 

@app.route("/user_restaurants")
def user_restaurants():
    restaurants = get_all_restaurants()
    return render_template("user_restaurants.html", count=len(restaurants), restaurants=restaurants) 

@app.route("/review")
def reviews():
    restaurants_all = get_reviews()
    return render_template("reviews.html", count=len(restaurants_all), restaurants=restaurants_all) 

@app.route("/add_review", methods=["POST"])
def reviews_to_db():
    restaurant_id = request.form.get('restaurant_id')
    stars = request.form.get('stars')
    comment = request.form.get('comment')

    if not stars:
        return redirect(request.referrer)
    
    add_review(restaurant_id, stars, comment)
    return redirect('/review')

@app.route("/send", methods=["POST"])
def send():
    name = request.form["name"]
    address = request.form["address"]
    city = request.form["city"]

    add_restaurant(name, address, city)
    
    return redirect("/restaurants")


@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    admins = users.check_for_admin_rights()
    admin_list = []
    admin_list.append(admins[0][1])

    if users.login(username,password) == False:
        flash('Invalid username or password')
        return redirect('/')

    if username not in admin_list:
       return redirect("/user_restaurants")
    
    else:
        return redirect("/restaurants")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/create_account", methods=["POST"])
def craete_account():
    username = request.form["username"]
    password = request.form["password"]

    if not username or not password:
        flash('Invalid username or password')
        return redirect('/')

    if len(username) < 4:
        flash('Username should be at least 4 characters')
        return redirect('/')
    
    if len(password) < 6:
        flash('Password should be at least 6 characters')
        return redirect('/')
    
    users.create_account(username,password)

    return redirect("/user_restaurants")

@app.route("/search", methods=["POST"])
def search():
    substring = request.form.get('name')
    filtered_restaurants = search_restaurants(substring)
    return render_template('filtered.html', count=len(filtered_restaurants), restaurants=filtered_restaurants)
    

@app.route("/delete", methods=["POST"])
def delete():
    restaurant_id = request.form.get('restaurant_id')
    delete_restaurant(restaurant_id)
    return redirect("/restaurants")
