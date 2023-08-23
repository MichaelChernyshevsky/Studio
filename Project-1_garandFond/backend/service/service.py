from data.counter import *
from data.order import *

#orders
def service_getOrders():
    return getOrders()

def service_addOrder(order):
    return addOrder(order)

def service_disposeOrderss():
    return disposeOrders()

#counter
def service_getCounter():
    return getCounter()

def service_increaseCounter():
    return increaseCounter()

def service_decreaseCounter():
    return decreaseCounter()


