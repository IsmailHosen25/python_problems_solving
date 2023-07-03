num=int(input())
for i in range(2,num+1):
    if(num%i==0):
        if(num==i):
            print("Yes")
            break
        else:
            print("No")
            break
    else:
        continue
