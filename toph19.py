# class Stack:
#     def __init__(self):
#         self.arr=[]
#     def push(self,n):
#         self.arr.append(n)
#     def isEmpty(self):
#         if(len(self.arr)==0):
#             return True
#         else:
#             return False
#     def pop(self):
#         if(self.isEmpty==True):
#             print("empty array ")
#         else:
#             self.arr.pop()
#     def display(self):
#         return self.arr
# a,b=map(str,input().split())
# first=Stack()
# snd=Stack()
# for i in range(len(a)):
#     first.push(a[i])
# for i in range(len(b)):
#     snd.push(b[i])


def has_carry(a, b):
    carry = 0
    while a > 0 or b > 0:
        sum_digits = a % 10 + b % 10 + carry
        if sum_digits >= 10:
            return True
        carry = sum_digits // 10
        a //= 10
        b //= 10
    return False
a, b = map(int, input().split())
if has_carry(a, b):
    print("Yes")
else:
    print("No")