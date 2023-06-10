str1=list(input())
str2=list(input())
if(len(str1)==len(str2)):
    for i in range(len(str1)-1,-1,-1):
        if(str1[i]in str2):
            if(i==0):
                print("Yes")
            else:
                continue
        else:
            print("No")
            break
else:
    print("No")
