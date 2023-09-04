from app import db

class Events (db.Model):
    __tablename__ = "toneevents"
    __table_args__ = {"extend_existing": True}

    id = db.Column("id", db.Integer, primary_key=True)
    type_id = db.Column("type_id", db.Integer,)
    place = db.Column("place", db.String(100))
    link = db.Column("link", db.String(300))


    def __init__(self,type_id, place,link):
        self.type_id = type_id
        self.place = place
        self.link = link

    @staticmethod
    def getEvents():
        try:
            json_events = []
            events = Events.query.all()
            for event in events:

                form = {
                    "id" : event.__dict__['id'],
                    "type_id" : event.__dict__['type_id'],
                    "place" : event.__dict__['place'],
                    "link" : event.__dict__['link'],
                }

                json_events.append(form)

            return json_events
        except:
            return 500
        
    @staticmethod
    def deleteEvent(id):
        event = Events.query.filter_by(id=id).first()
        db.session.delete(event)
        db.session.commit()

        

    @staticmethod
    def addEvent(type_id, place,link):
        card = Events(
            type_id=type_id,
            place=place,
            link=link,
            )
        db.session.add(card)
        db.session.commit()
     
 
   