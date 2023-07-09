
roll=int(input())
c=0
for i in range(1,roll):
    if(roll%i==0):
        c=c+1
    else:
        continue
print(c)