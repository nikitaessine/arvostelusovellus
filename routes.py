from flask import render_template, request, redirect, flash
from sqlalchemy.sql import text
from app import app
from db import db
from restaurants import search_restaurants, delete_restaurant, add_review
import users

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/new")
def new():
    return render_template("new.html")

    
@app.route("/restaurants")
def restaurants():
    result = db.session.execute(text("SELECT * FROM restaurants"))
    restaurants = result.fetchall()
    return render_template("restaurants.html", count=len(restaurants), restaurants=restaurants) 

@app.route("/user_restaurants")
def user_restaurants():
    result = db.session.execute(text("SELECT * FROM restaurants"))
    restaurants = result.fetchall()
    return render_template("user_restaurants.html", count=len(restaurants), restaurants=restaurants) 

@app.route("/review")
def reviews():
    result = db.session.execute(text("SELECT restaurants.*, AVG(reviews.stars) AS avg_stars, COUNT(reviews.id) AS review_count FROM restaurants LEFT JOIN reviews ON restaurants.id = reviews.restaurant_id GROUP BY restaurants.id"))
    restaurants_all = result.fetchall()
    return render_template("reviews.html", count=len(restaurants_all), restaurants=restaurants_all) 

@app.route("/add_review", methods=["POST"])
def reviews_to_db():
    restaurant_id = request.form.get('restaurant_id')
    user_id = request.form.get('user_id')
    stars = request.form.get('stars')
    comment = request.form.get('comment')

    if not stars:
        # If stars field is empty, stay on the same page
        return redirect(request.referrer)
    
    add_review(user_id, restaurant_id, stars, comment)
    return redirect('/review')

@app.route("/send", methods=["POST"])
def send():
    name = request.form["name"]
    sql = text("INSERT INTO restaurants (name) VALUES (:name)")
    db.session.execute(sql, {"name":name})
    db.session.commit()
    return redirect("/restaurants")


@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    admin_or_not = db.session.execute(text("SELECT * FROM users WHERE admin = TRUE"))
    admins = admin_or_not.fetchall()

    admin_list = []
    admin_list.append(admins[0][1])

    if users.login(username,password) == False:
        flash('Invalid username or password')
        return redirect('/')

    elif username not in admin_list:
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
        flash('Username should be at least 6 characters')
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
