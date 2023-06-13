str=list(input())
for i in range(len(str)):
    str[0]=str[0].upper()
    if(str[i]=="s" or str[i]=="i" or str[i]=="o"):
        if(str[i]=="s"):
            str[i]="$"
        elif(str[i]=="i"):
            str[i]="!"
        else:
            str[i]="()"
    else:
        continue
str.append(".")
result="".join(str)
print(result)