# Import necessary packages
import time
from collections import deque
from threading import Thread

# First implementation.
class Queue1:
    def __init__(self):
        self.buffer = deque()
        
    def enqueue(self, item):
        self.buffer.appendleft(item)
        
    def dequeue(self):
        return self.buffer.pop()
    
    
    def isEmpty(self):
        return len(self.buffer) == 0
    
    def length(self):
        return len(self.buffer)


# Place and Serve order program...
psQ = Queue1()

def placeOrders(orders):
    for order in orders:
        print(f"Placing order for: {order}")
        psQ.enqueue(order)
        time.sleep(1)


def serveOrders():
    time.sleep(1.5)
    for i in range(len(orders)):
        order = psQ.dequeue()
        print(f"Serving: {order}")
        time.sleep(3)


# New Queue class with slight modifications.
class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if len(self.buffer)==0:
            print("Queue is empty")
            return
        return self.buffer.pop()

    def isEmpty(self):
        return len(self.buffer) == 0

    def length(self):
        return len(self.buffer)

    def prime(self):
        return self.buffer[-1]

# Binary number program.
def generateBinaries(r):
    bQ = Queue()
    bQ.enqueue("1")

    for i in range(r):
        prime = bQ.prime()
        print(f"{prime}")
        bQ.enqueue(f"{prime}0")
        bQ.enqueue(f"{prime}1")

        bQ.dequeue()

if __name__ == '__main__':
    # Binary number program.
    generateBinaries(15)

    # Place and Serve order program.
    orders = ['jollof', 'garri', 'eba', 'okra', 'amala']
    placingT = Thread(target=placeOrders, args=(orders,))
    servingT = Thread(target=serveOrders)

    placingT.start()
    servingT.start()


# ifunanyaScript