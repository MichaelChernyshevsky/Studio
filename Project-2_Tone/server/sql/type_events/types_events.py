from app import db

class Type (db.Model):
    __tablename__ = "tonetypes"
    __table_args__ = {"extend_existing": True}

    id = db.Column("id", db.UUID, primary_key=True)
    type = db.Column("type", db.String(100))
 


    def __init__(self,type):
        self.type = type

    @staticmethod
    def getTypes():
        try:
            json_events = []
            events = Type.query.all()
            for event in events:

                form = {
                    "id" : event.__dict__['id'],
                    "type" : event.__dict__['type'],
                   
                }

                json_events.append(form)

            return json_events
        except:
            return 500
        
    @staticmethod
    def checkId(id):
       pass
        
    @staticmethod
    def deleteType(id):
        event = Type.query.filter_by(id=id).first()
        db.session.delete(event)
        db.session.commit()

        

    @staticmethod
    def addType(type):
        card = Type(type=type)
        db.session.add(card)
        db.session.commit()
     
 
   