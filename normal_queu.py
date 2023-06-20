class queue:
    def __init__(self):
        self.arr=[]
    def enquiue(self,str):
        self.arr.append(str)
    def dequeue(self):
        self.arr.pop(0)
    def print_queue(self):
        return self.arr
h=queue()
h.enquiue(12)
h.enquiue(87)
h.enquiue(54)
print(h.print_queue())
h.dequeue()
h.enquiue(67)
print(h.print_queue())