from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from app import app
from models.order import Order
from models.counter import Counter


# order
@app.route("/read/orders")
def readOrders():
    return jsonify(Order.getOrders())


@app.delete("/delete")
def delete():
    Order.disposeOrders()
    return jsonify(Order.getOrders())


@app.put("/orders/add")
def putAddOrder():
    Order.addOrder(request.json["contact"], request.json["comment"])
    return jsonify(Order.getOrders())


# counter
@app.route("/read/counter")
def readCounter():
    return jsonify(Counter.getCounter())


@app.put("/counter/increase")
def putIncreaseCounter():
    Counter.increaseCounter()
    return jsonify(Counter.getCounter())


@app.put("/counter/decrease")
def putDecreaseCounter():
    Counter.decreaseCounter()
    return jsonify(Counter.getCounter())


if __name__ == "__main__":
    app.run(debug=True, port=5001)
