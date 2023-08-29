from flask import Flask,request,jsonify
from service.service import Service

app = Flask(__name__)


@app.put('/addCard')
def addCard():
    card =  {
                "date" : request.json["connection"],
                "place":request.json["comment"],
                "direction": request.json["direction"],
                "index": str(Service.getLenCards())
            }
    Service.addCard(card=card)
@app.delete('/delete/<int:index>')
def deleteCard(index):
    Service.deleteCard(index=index)

@app.get('/filter/data')
def filterData():
    return jsonify(Service.filterData())

@app.get('/filter/<str:place>')
def filterPlace(place):
    return jsonify(Service.filterPlace(place=place))

@app.get('/filter/<str:event>')
def filterEvent(event):
    return jsonify(Service.filterEvent(event=event))

if __name__ == "__main__":
    app.run(debug=True,port=5001)



