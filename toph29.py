n=int(input())
a=[]
b=[]
for i in range(n):
   x,y=map(int,input().split())
   a.append(x)
   b.append(y)
for i in range(len(a)):
   avg=(a[i]+b[i])//2
   if(avg%2==0):
      print("Sadia will be happy.")
   else:
      print("Oops!")

