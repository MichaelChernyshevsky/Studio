from server import Order,db


def getIndex():
    return Order.query.count()+1
    
def getOrders():
    return Order.query.all()

def addOrder(contact,comment):
    order = Order(id=getIndex(),contact=contact,comment=comment)
    db.session.add(order)
    db.session.commit()

def disposeOrders():
    db.session.query(Order).delete()
    db.session.commit()

