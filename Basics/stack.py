from collections import deque
stack = deque()
#print(dir(stack))
#stack.append(1)
#stack.append(2)
#print(stack.pop())

class Stack:
    def __init__(self):
        self. container = deque()
    
    def push(self, data):
        self.container.append(data)
    
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)


if __name__=="__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    print(stack.peek())
    print(stack.pop())
    print(stack.size())






