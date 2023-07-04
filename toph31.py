index,start,end=map(int,input().split())
l=list(map(int,input().split()))
result=0
for i in range(start,end+1):
    result=result+l[i]
print(result)