### Q-1
class stack:
    def __init__(self):
        self.arr=[]
    def push(self,str):
        for i in range (len(str)):
            self.arr.append(str[i])
    def print_stack(self):
          return self.arr
    def isempty(self):
        if(len(self.arr) == 0):
            return True
        else:
            return False
    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
           self.arr.pop()
    def peek(self):
        if self.isempty():
            print("Stack is empty")
        else:
            return self.arr[-1]
str=input()

def rev_str(str):
    convert_list=stack()
    convert_list.push(str)
    str1=convert_list.print_stack()
    rev_str=''
    for i in range(len(str1)-1,-1,-1):
       rev_str=rev_str+str1[i]
    return rev_str
print(rev_str(str))