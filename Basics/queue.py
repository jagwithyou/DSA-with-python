#list as queue
def list_as_queue():
    stock_price=[]
    stock_price.insert(0, 1)
    stock_price.insert(0, 2)
    stock_price.insert(0, 3)
    print(stock_price.pop())
    print(stock_price.pop())

from collections import deque
def using_deque():
    queue = deque()

    queue.appendleft(1)
    queue.appendleft(2)
    queue.appendleft(3)
    print(queue.pop())

class Queue:
    def __init__(self):
        self.container = deque()
    
    def enque(self, data):
        self.container.appendleft(data)
    
    def deque(self):
        return self.container.pop()
    
    def is_empty(self):
        return len(self.container)==0

    def size(self):
        return len(self.container)

if __name__=="__main__":
    queue = Queue()
    queue.enque(1)
    queue.enque(2)
    print(queue.deque())