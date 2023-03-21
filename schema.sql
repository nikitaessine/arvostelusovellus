CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);

CREATE TABLE restaurants(
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY, 
    user_id INTEGER REFERENCES users, 
    restaurant_id INTEGER REFERENCES restaurants, 
    stars INTEGER, 
    comment TEXT
);