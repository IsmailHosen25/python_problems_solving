class Node:
   def __init__(self,value):
      self.value=value
      self.next=None
class sgll:
    def __init__(self):
      self.head=None
      self.till=None
      self.size=0
    def append(self,value):
        newNode=Node(value)
        if(self.head==None ):
           self.head=newNode
           self.till=newNode
           self.size+=1
        else:
           current=self.head
           while current != None:
              if(current.next==None):
                 current.next=newNode
                 self.till=newNode
                 self.size+=1
                 break
              else:
                 current=current.next
    def add_first(self,value):
        newNode=Node(value)
        if(self.head==None):
           self.head=newNode;
           self.till=newNode
           self.size+=1
        else:
           newNode.next=self.head
           self.head=newNode
           self.size+=1
    def insrt_after_x(self,x,value):
       newNode=Node(value)
       if(self.head==None):
          self.head=newNode
          self.till=newNode
          self.size+=1
       else:
            if(self.till.value==x):
               self.append(value)
            else:
               current=self.head
               while current.next!=None:
                 if(current.value==x):
                    newNode.next=current.next
                    current.next=newNode
                    self.size+=1
                    break
                 else:
                   current=current.next
    def insert_befor_x(self,x,value):
        newNode=Node(value)
        if(self.head==None):
           self.head=newNode
           self.till=newNode
           self.size+=1
        else:
            if(self.head.value==x):
                   self.add_first(value)
            else:
               current=self.head
               while current.next!=None:
                  if(current.next.value==x):
                     newNode.next=current.next
                     current.next=newNode
                     self.size+=1
                     break
                  else:
                    current=current.next
    def pop(self):
       current=self.head
       while current.next!=None:
            if(current.next.next==None):
               current.next=None
               self.till=current
               self.size-=1
               return current.value
            else:
               current=current.next
               
    def remove_first(self):
       self.head=self.head.next
       self.size-=1
    def remove_x(self,x):
        if(self.head.value==x):
           self.remove_first()
        elif(self.till.value==x):
           self.pop()
        else:
           current=self.head
           while current.next!=None:
             if(current.next.value==x):
               current.next=current.next.next
               self.size-=1
               break
             else:
               current=current.next
    def deleteEven(self):
         current=self.head
         if(current.value%2==0):
           self.head=current.next
         while current !=None:
               if (current.next!=None and current.next.value%2==0):
                    t=current.next.next
                    current.next=t
               else:
                  current=current.next
                
    def sortedInsert(self,x):
       newNode=Node(x)
       current=self.head
       while current !=None:
              if(current.value>x):
                 newNode.next=self.head
                 self.head=newNode
                 break
              elif(current.value<x and current.next !=None and current.next.value>x):
                 newNode.next=current.next
                 current.next=newNode
                 break
              elif(current.value<x and current.next==None):
                 current.next=newNode
                 break
              else:
                 current=current.next
    def size_sgll(self):
       return self.size
    def print_sgll(self):
        if(self.head==None):
           print("linked list is empty")
        else:
            current=self.head
            print("Head -> ",end="")
            while current.next != None:
                print(current.value,end=" -> ")
                current=current.next
            print(current.value,end=" -> None\n")
    def getAvarage(self):
        current=self.head
        sum=0
        while current != None:
           sum=sum+current.value
           current=current.next
        avg=sum/self.size
        return avg
    def numOfOcurrences(self,x):
        current=self.head
        c=0
        while current!=None :
            if(current.value==x):
              c+=1
              current=current.next
            else:
               current=current.next
        return c
    def reverse(self):
        prev = None
        current = self.head   
        while current !=None:
            t = current.next
            current.next = prev
            prev = current
            current = t
        self.head = prev
   #  def sort_the_sll(self):
   #      cur=self.head
   #      while cur!=None:
   #          if(cur.value>cur.next.value and cur==self.head):
   #            t=cur.next.next
   #            cur.next.next=cur
   #            cur.next=t
   #            self.head=cur.next.next
   #            cur=self.head
   #          elif(cur.value>cur.next.value and cur.next !=None):
   #            t=cur.next.next
   #            cur.next.next=cur
   #            cur.next=t
   #            cur=self.head
   #          else:
   #             cur=cur.next
    
s1=sgll()
s1.append(10)
s1.append(6)
s1.append(7)
s1.append(8)
s1.append(6)
s1.print_sgll()
s1.reverse()
s1.print_sgll()
# s2=sgll()
# s2.append(3)
# s2.append(6)
# s2.append(7)
# s2.append(10)
# s2.print_sgll()
# s2.sortedInsert(5)
# s2.print_sgll()

print("shorted insert")
s3=sgll()
s3.append(3)
s3.sortedInsert(5)
s3.sortedInsert(4)
s3.sortedInsert(1)
s3.sortedInsert(6)
s3.print_sgll()
# def equalNode(s1,s2):
#     if(s1.size_sgll()==s2.size_sgll()):
#         cur_1=s1.head
#         cur_2=s2.head
#         s=True
#         while cur_1!=None:
#             if(cur_1.value==cur_2.value):
#                cur_1=cur_1.next
#                cur_2=cur_2.next
#             else:
#                 s=False
#                 break
#         return s
#     else:
#        return False
# print(equalNode(s1,s2))