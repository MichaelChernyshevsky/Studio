from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


from app import app
from data.data import Card
from events.events import Events




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
        event = request.json["event"],
        )
    return jsonify(Card.getCards())

@app.get('/filter/place')
def filterPlace():
    return jsonify(Card.filterPlace(place=request.json["place"]))

@app.get('/filter/date')
def filterData():
    return jsonify(Card.filterDate())

@app.get('/filter/event')
def filterEvent():
    return jsonify(Card.filterEvent(event=request.json["event"]))




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
        type = request.json["type"],
        place = request.json["place"],
        link = request.json["link"],
        )
    return jsonify(Events.getEvents())

if __name__ == "__main__":
    app.run(debug=True,port=5001)
