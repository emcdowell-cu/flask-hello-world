from flask import Flask
app = Flask(__name__)

import psycopg2

@app.route('/')
def hello_world():
    return 'Hello, Worldfrom Elsa McDowell in 3308.'


@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://emcdowell_db_user:TAAFXHs5Q6Zg07Xdoy8LJg197XOuh3DN@dpg-cqfsksdds78s73c50a6g-a/emcdowell_db")
    conn.close()
    return 'Database Connection Successful'

@app.route('/db_create')
def create():
    conn = psycopg2.connect("postgresql://emcdowell_db_user:TAAFXHs5Q6Zg07Xdoy8LJg197XOuh3DN@dpg-cqfsksdds78s73c50a6g-a/emcdowell_db")
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
    ''')
    conn.commit()
    conn.close()
    return 'Basketball table created successfully'