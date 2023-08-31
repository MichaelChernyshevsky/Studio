from app import db

class Card (db.Model):
    __tablename__ = "tone"
    __table_args__ = {"extend_existing": True}

    id = db.Column("id", db.Integer, primary_key=True)
    minutes = db.Column("minutes", db.Integer)
    hour = db.Column("hour", db.Integer)
    mounth = db.Column("mounth", db.Integer)
    year = db.Column("year", db.Integer)
    day = db.Column("day", db.Integer)
    place = db.Column("place", db.String(100))
    event = db.Column("event", db.String(100))
    data = db.Column( "data", db.DateTime)

    def __init__(self,minutes, hour,day,place,mounth,year,event,date):
        self.minutes = minutes
        self.mounth = mounth
        self.hour = hour
        self.day = day
        self.place = place
        self.year = year
        self.event = event
        self.date = date

    def convertData(minutes, hour,day,mounth,year,):
        pass
    
    def toJson(items):
        elements= []
         
        for card in items:
            form = {
                    "id" :  card.__dict__["id"],
                    "minutes" : card.__dict__["minutes"],
                    "hour": card.__dict__["hour"],
                    "day": card.__dict__["day"],
                    "mounth" : card.__dict__["mounth"],
                    "year" : card.__dict__["year"],
                    "place" : card.__dict__["place"],
                    "event" : card.__dict__["event"],
                    "data" : card.__dict__['data']
            }
            elements.append(form)
        
        return elements

    @staticmethod
    def addCard(minutes,hour,day,place,event,year,mounth):
        card = Card(
            mounth=mounth,
            year=year,
            minutes=minutes,
            hour=hour,
            day=day,
            place=place,
            event=event,
            date=Card.convertData(minutes,hour,day,mounth,year,)
            )
        db.session.add(card)
        db.session.commit()
     
    @staticmethod
    def deleteCard(id):
        card = Card.query.filter_by(id=id).first()
        db.session.delete(card)
        db.session.commit()

    @staticmethod
    def filterDate():
        pass

    @staticmethod
    def filterPlace(place):
        cards = Card.query.filter_by(place=place)
        return Card.toJson(items = cards )
        
    @staticmethod
    def filterEvent(event):
        cards = Card.query.filter_by(event=event)
        return Card.toJson(items = cards )

    @staticmethod
    def getCards():
        try:
            cards = Card.query.all()
            return Card.toJson(items = cards )
        except:
            return 500

        
