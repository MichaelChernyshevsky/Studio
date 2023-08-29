class Cards:
    global cards

    cards = [
        {
                "date" : "1",
                "place": "1",
                "direction":  "1",
                "index":"1"
            }
    ]


    def addCard(card):
        cards.append(card)
    def getLenCards():
        return len(cards)
    def deleteCard(index):
        cards.pop(index-1)

    def filterData():
        pass

    def filterPlace(place):
        pass
    
    def filterEvent(event):
        pass

        
