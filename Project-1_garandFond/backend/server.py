from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy

from service.service import Service

from server import db

app = Flask(__name__)

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



#order
@app.route('/read/orders')
def readOrders():
    return jsonify(Service.getOrders())
@app.delete('/delete')
def delete():
    Service.disposeOrderss()
    return jsonify(Service.getOrders())
@app.put('/orders/add')
def addOrder():
    Service.addOrder(request.json["contact"],request.json["comment"])
    return jsonify(Service.getOrders())

# counter
@app.route('/read/counter')
def readCounter():
    return jsonify(Service.getCounter())
@app.put('/counter/increase')
def increaseCounter():
    Service.increaseCounter()
    return jsonify(Service.getCounter())
@app.put('/counter/decrease')
def decreaseCounter():
    Service.decreaseCounter()
    return jsonify(Service.getCounter())



if __name__ == "__main__":
    app.run(debug=True,port=5001)

