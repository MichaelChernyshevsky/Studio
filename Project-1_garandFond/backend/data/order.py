orders = [
            {
                "connection" : "+798982123211",
                "comment":"somecomment"
            }
        ]
    

def getOrders():
    return orders


def addOrder(order):
    orders.append(order)

def disposeOrders():
    global orders
    orders = []