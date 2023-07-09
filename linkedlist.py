class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class sgll:
    def __init__(self):
        self.head=None
    def addlast(self,value):
       newNode=Node(value)
       if(self.head==None):
           self.head=newNode
       else:
            cur=self.head
            while cur.next!= None:
               cur=cur.next
            cur.next=newNode
    def addfirst(self,value):
        newNode=Node(value)
        if(self.head==None):
            self.head=newNode
        else:
           newNode.next = self.head
           self.head = newNode
    def add_after_x(self,x,value):
        newNode=Node(value)
        t=None
        cur=self.head
        while cur.next !=None:
            if(cur.value==x):
                t=cur.next
                break
            else:
                cur=cur.next
        newNode.next=t
        cur.next=newNode
    def add_befor_x(self,x,value):
        newNode=Node(value)
        t=None
        cur=self.head
        while cur.next !=None:
            if(cur.next.value==x):
                t=cur.next
                break
            else:
                cur=cur.next
            newNode.next=t
            cur=newNode
    def print_ll(self):
        cur=self.head
        if(cur==None):
            print("ll is empty")
        else:
            while (cur != None):
               print(cur.value,end="->")
               cur=cur.next
            print()
s=sgll()
s.addlast(10)
s.addlast(15)
s.addlast(20)
s.print_ll()
s.addfirst(50)
s.addfirst(100)
s.print_ll()
s.add_after_x(10,200)
s.print_ll()

        