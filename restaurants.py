from flask import abort, session, request
from sqlalchemy.sql import text
from db import db

def search_restaurants(substring):
    sql = text("SELECT * FROM restaurants WHERE LOWER(name) LIKE '%' || LOWER(:substring) || '%'")
    result = db.session.execute(sql, {"substring":substring})
    filtered_restaurants = result.fetchall()
    print(filtered_restaurants)

    return filtered_restaurants 

def delete_restaurant(restaurant_id):
    sql = text("DELETE FROM restaurants WHERE id=:restaurant_id")
    db.session.execute(sql, {"restaurant_id":restaurant_id})
    db.session.commit()
 

    