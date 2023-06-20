# a,b=map(int , input().split())
# n=(a+b)%2
# if(n==0):
#     print("Black")
# else:
#     print("White")

a, b = input().split()
x = int(a[-1]) + int(b[-1])
print("Black" if x % 2 == 0 else "White")