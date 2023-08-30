from app import db


class Order(db.Model):
    __tablename__ = "orders"
    __table_args__ = {"extend_existing": True}

    id = db.Column("id", db.Integer, primary_key=True)
    contact = db.Column("contact", db.String(100))
    comment = db.Column("comment", db.String(500))

    def __init__(self, id, contact, comment):
        self.id = id
        self.contact = contact
        self.comment = comment

    @staticmethod
    def getIndex():
        return Order.query.count() + 1

    @staticmethod
    def getOrders():
        orders = Order.query.all()
        json_orders = []
        for order in orders:
            form = {
                "contact": order.__dict__["contact"],
                "comment": order.__dict__["comment"],
            }
            json_orders.append(form)
        return json_orders

    @staticmethod
    def addOrder(contact, comment):
        order = Order(id=Order.getIndex(), contact=contact, comment=comment)
        db.session.add(order)
        db.session.commit()

    @staticmethod
    def disposeOrders():
        db.session.query(Order).delete()
        db.session.commit()
