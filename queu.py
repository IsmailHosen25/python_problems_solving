class Stack:

    def __init__(self):
        self.arr = []

    def push(self, str):
        self.arr.append(str)

    def pop(self):
        return self.arr.pop()

    def size(self):
        return len(self.arr)

    def is_empty(self):
        if(len(self.arr)==0):
            return True
        else:
            return False
    def print_stack(self):
        return self.arr
    def size(self):
        return len(self.arr)

class Queue:

    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def enqueue(self, str):
        self.in_stack.push(str)

    def dequeue(self):
        for i in range(self.in_stack.size()-1,0,-1):
           self.out_stack.push(self.in_stack.pop())
        self.in_stack.pop()
        for i in range(self.out_stack.size()):
           self.in_stack.push(self.out_stack.pop())
    def print_queue(self):
        q=self.in_stack.print_stack()
        return q
q = Queue()
q.enqueue(7)
q.enqueue(8)
q.enqueue(3)
q.enqueue(5)
print(q.print_queue())
q.dequeue()
q.dequeue()
print(q.print_queue())
q.enqueue(12)
print(q.print_queue())

