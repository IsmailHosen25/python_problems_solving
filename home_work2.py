### Q-1
# class stack:
#     def __init__(self):
#         self.arr=[]
#     def push(self,str):
#         for i in range (len(str)):
#             self.arr.append(str[i])
#     def print_stack(self):
#           return self.arr
#     def isempty(self):
#         if(len(self.arr) == 0):
#             return True
#         else:
#             return False
#     def pop(self):
#         if self.isempty():
#             print("Stack is empty")
#         else:
#            self.arr.pop()
#     def peek(self):
#         if self.isempty():
#             print("Stack is empty")
#         else:
#             return self.arr[-1]
# str=input()

# def rev_str(str):
#     convert_list=stack()
#     convert_list.push(str)
#     str1=convert_list.print_stack()
#     rev_str=''
#     for i in range(len(str1)-1,-1,-1):
#        rev_str=rev_str+str1[i]
#     return rev_str
# print(rev_str(str))


##Q-2

# brackets = input()
# stack = []
# for b in brackets:
# 	if b == '(' or b=="{" or b=="[":
# 		stack.append(b)
# 	else:
# 		if len(stack) > 0:
# 			stack.pop()
# 		else:
# 			stack.append(b)
# 			break

# if len(stack) == 0:
# 	print(True)
# else:
# 	print(False)

###Q-3
# class Stack:
#     def __init__(self):
#         self.arr=[]
#     def push(self,str):
#             self.arr.append(str)
#     def print_stack(self):
#           return self.arr
#     def size(self):
#         return len(self.arr)
#     def isempty(self):
#         if(len(self.arr) == 0):
#             return True
#         else:
#             return False
#     def pop(self):
#         if self.isempty():
#             print("Stack is empty")
#         else:
#            self.arr.pop()
#     def peek(self):
#         if self.isempty():
#             print("Stack is empty")
#         else:
#             return self.arr[-1]
# lst=[7,9,4,8,14,56,8,3,2,0]
# lst_max=lst[0]
# new_stack=Stack()
# for i in range (1,len(lst)):
#     if(lst_max<lst[i]):
#         new_stack.push(lst_max)
#         lst_max=lst[i]
#     else:
#         new_stack.push(lst[i])
# new_stack.push(lst_max)
# print(new_stack.print_stack())

## Q-4

A=[1,5,11,4]
B=[4,32,-1,1]
a_sum=0
b_sum=0
add=0
for i in range(len(A)):
    a_sum=a_sum+A[i]
for i in range(len(B)):
    b_sum=b_sum+B[i]
if(a_sum>b_sum):
    add=a_sum-b_sum
    A.append(add)
else:
    add=b_sum-a_sum
    B.append(add)
print(A,B,sep='\n')