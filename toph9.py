n= int(input())
note=[500,100,50,10,5,1]
result =[]
for i in note:
    temp=[]
    sub = int(n/i)
    rest = int(n%i)
    if rest == 0:
        temp = [i]*sub
        result.extend(temp)
        break
    else:
        temp = [i] * sub
        result.extend(temp)
        n = rest

result.sort()
for i in result:
    print(i,end=" ")