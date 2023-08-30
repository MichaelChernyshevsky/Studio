from app import db


class Counter(db.Model):
    __tablename__ = "counter"
    __table_args__ = {"extend_existing": True}

    id = db.Column("id", db.Integer, primary_key=True)
    count = db.Column("count", db.Integer)

    def __init__(self, id, count):
        self.id = id
        self.count = count

    @staticmethod
    def getCounter():
        return Counter.query.filter_by(id=1).first().__dict__["count"]

    @staticmethod
    def increaseCounter():
        counter = Counter.query.filter_by(id=1).first()
        counter.count += 1
        db.session.commit()

    @staticmethod
    def decreaseCounter():
        counter = Counter.query.filter_by(id=1).first()
        counter.count -= 1
        db.session.commit()
