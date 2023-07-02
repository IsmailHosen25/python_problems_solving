import math
n=int(input())
a=[]
b=[]
for i in range(n):
	x,y=map(int,input().split())
	a.append(x);b.append(y)
d=10<<500
for i in range(n):
	for j in range(i+1,n):
		x=math.sqrt((a[i]-a[j])**2+(b[i]-b[j])**2)
		if x<d:
			d=x	
print(d)