from datetime import datetime
from flask import Flask,render_template,url_for,request,jsonify
from service.service import *

app = Flask(__name__)

#order
@app.route('/read/orders')
def readOrders():
    return jsonify(service_getOrders())

@app.delete('/delete')
def delete():
    service_disposeOrderss()
    return jsonify([])

@app.put('/orders/add')
def addOrder():
    order =  {
                "connection" : request.json["connection"],
                "comment":request.json["comment"],
            }
    service_addOrder(order)
    return jsonify(service_getOrders())

# counter
@app.route('/read/counter')
def readCounter():
    return jsonify(service_getCounter())

@app.put('/counter/increase')
def increaseCounter():
    service_increaseCounter()
    return jsonify(service_getCounter())

@app.put('/counter/decrease')
def decreaseCounter():
    service_decreaseCounter()
    return jsonify(service_getCounter())

if __name__ == "__main__":
    app.run(debug=True,port=5001)

