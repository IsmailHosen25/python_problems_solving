n=int(input())
m=1000000007
a=int(((n**2)+n)/2)%m
print(a,end=" ")
b=(n**n)%m
print(b,end=" ")
c=1
for i in range(1,n+1):
    c=(c*i)%m
print(c,end=" ")
d=((2**n)+(3**n))%m
print(d)