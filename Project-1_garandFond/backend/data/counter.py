global counter 



counter = 10


def getCounter():
    return counter

def increaseCounter():
    global counter

    counter += 1

def decreaseCounter():
    global counter
    if counter > 0:
        counter -= 1
