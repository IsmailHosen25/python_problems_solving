h,m=map(int , input().split())
degree=30*h-(11/2)*m
if(degree>180):
    degree=360-degree
print(f"{degree:.7f}")