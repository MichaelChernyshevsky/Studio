from server import Counter,db


def getCounter():
    return Counter.query.filter_by(id=1).first().__dict__['count']

def increaseCounter():
    counter = Counter.query.filter_by(id = 1).first()
    counter.count += 10
    db.session.commit()

def decreaseCounter():
    counter = Counter.query.filter_by(id = 1).first()
    counter.count -= 10
    db.session.commit()

getCounter()