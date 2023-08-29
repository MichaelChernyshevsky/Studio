from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from psycopg2 import *

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost/mydb"
    app.app_context().push()
    return app

app =  create_app()
db = SQLAlchemy(app)


class Counter(db.Model):
    __tablename__  = "counter"
    __table_args__ = {'extend_existing': True}
   

    id = db.Column('id',db.Integer,primary_key = True)
    count = db.Column('count',db.Integer)

    def __init__(self,id,count):
        self.id = id
        self.count = count


class Order(db.Model):
    __tablename__  = "orders"
    __table_args__ = {'extend_existing': True}
   

    id = db.Column('id',db.Integer,primary_key = True)
    contact = db.Column('contact',db.String(100))
    comment = db.Column('comment',db.String(500))


    def __init__(self,id,contact,comment):
        self.id = id
        self.contact = contact
        self.comment = comment
