from data.data import Cards

class Service:
    
    def addCard(card):
        Cards.addCard(card=card)

    def getLenCards():
        return  Cards.getLenCards()+2
    
    def deleteCard(index):
        Cards.deleteCard(index=index)

    def filterData():
        return Cards.filterData()

    def filterPlace(place):
        return Cards.filterPlace(place=place)
    
    def filterEvent(event):
        return Cards.filterEvent(event=event)
