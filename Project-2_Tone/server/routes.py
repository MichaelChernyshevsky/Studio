from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


from app import app
from sql.card.data import Card
from sql.event.events import Events
from sql.type_events.types_events import Type




# ---------------------------------------------------
@app.get('/cards')
def getCards():
   return jsonify(Card.getCards())

@app.delete('/deleteCard')
def deleteCard():
   Card.deleteCard(id=request.json["id"])
   return jsonify(Card.getCards())

@app.put('/addCard')
def addCard():
    Card.addCard(
        minutes=request.json["minutes"],
        hour = request.json["hour"],
        day = request.json["day"],
        mounth = request.json["mounth"],
        year= request.json["year"],
        place = request.json["place"],
        type_id = request.json["type_id"],
        )
    return jsonify(Card.getCards())

@app.get('/filter/place')
def filterPlace():
    return jsonify(Card.filterPlace(place=request.json["place"]))

@app.get('/filter/date')
def filterData():
    return jsonify(Card.filterDate())

@app.get('/filter/event')
def filterType():
    return jsonify(Card.filterType(type_id=request.json["type_id"]))




# ---------------------------------------------------
@app.get('/events')
def getEvents():
   return jsonify(Events.getEvents())

@app.delete('/deleteEvent')
def deleteEvent():
   Events.deleteEvent(id=request.json["id"])
   return jsonify(Events.getEvents())

@app.put('/addEvent')
def addEvent():
    Events.addEvent(
        type_id = request.json["type_id"],
        place = request.json["place"],
        link = request.json["link"],
        )
    return jsonify(Events.getEvents())
# ---------------------------------------------------
@app.get('/types')
def getTypes():
   return jsonify(Type.getTypes())

@app.delete('/deleteType')
def deleteTypes():
   Type.deleteType(id=request.json["id"])
   return jsonify(Type.getTypes())

@app.put('/addType')
def addTypes():
    Type.addType(
        type = request.json["type"],
        )
    return jsonify(Type.getTypes())

if __name__ == "__main__":
    app.run(debug=True,port=5001)
