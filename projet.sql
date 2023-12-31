
CREATE DATABASE stock_management;


CREATE TABLE IF NOT EXISTS products(
        product_id serial PRIMARY KEY,
        amount INTEGER,
        product_name VARCHAR(50),
        price FLOAT
    );

INSERT INTO products (amount, product_name, price)
VALUES
    (100, 'Ordinateur portable', 800.00),
    (50, 'Souris sans fil', 20.00),
    (75, 'Clavier mécanique', 50.00),
    (200, 'Écran LED 24 pouces', 150.00),
    (30, 'Casque audio Bluetooth', 70.00);



CREATE TABLE IF NOT EXISTS transactions(
        transaction_id serial PRIMARY KEY,
        product_id INTEGER,
        company_id INTEGER,
        amount INTEGER,
        product_name VARCHAR(50),
        cost INTEGER,
        company_name VARCHAR(50)
    );

INSERT INTO transactions (product_id, amount, product_name, company_name, cost,company_id)
VALUES
    (1, 10, 'Ordinateur portable', 'ABC Electronics', 7500,1),
    (2, 20, 'Souris sans fil', 'TechStore', 400,2),
    (3, 5, 'Clavier mécanique', 'Office Solutions', 250,3),
    (4, 15, 'Écran LED 24 pouces', 'Gadget Shop', 2250,4),
    (5, 2, 'Casque audio Bluetooth', 'SoundZone', 140,5);

CREATE TABLE IF NOT EXISTS company(
        company_id serial PRIMARY KEY,
        company_name VARCHAR(50),
        budget FLOAT 
    );


INSERT INTO companies (company_name, budget)
VALUES
    ('ABC Electronics', 5000.00),
    ('TechStore', 3000.00),
    ('Office Solutions', 1000.00),
    ('Gadget Shop', 8000.00),
    ('SoundZone', 2000.00);