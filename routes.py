from flask import render_template, request, redirect, flash
from sqlalchemy.sql import text
from app import app
from db import db
from restaurants import search_restaurants
import users

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/new")
def new():
    return render_template("new.html")

    
@app.route("/restaurants")
def restaurants():
    result = db.session.execute(text("SELECT name FROM restaurants"))
    restaurants = result.fetchall()
    return render_template("restaurants.html", count=len(restaurants), restaurants=restaurants) 


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

    if users.login(username,password) == False:
        return redirect("/")

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
    users.create_account(username,password)

    return redirect("/restaurants")

@app.route("/search", methods=["POST"])
def search():
    substring = request.form.get('name')
    filtered_restaurants = search_restaurants(substring)
    return render_template('filtered.html', count=len(filtered_restaurants), restaurants=filtered_restaurants)
    
