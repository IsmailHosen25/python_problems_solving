def check(x):
    if len(x)%2!=0:
        return 0
    if x=='':
        return 1

    try:
        for i in range(len(x)):
            if i == len(x)-1:
                break
            if (x[i]=='(' and x[i+1]==')') or (x[i]=='{' and x[i+1]=='}') or (x[i]=='[' and x[i+1]==']'):
                y=x[:i]
                z=x[i+2:]
                x=y+z
                if check(x)==1:
                    return 1
    except:
        return 0
    return 0

x = input()
if len(x)<=25:
    if x=="":
        print("No")
    elif check(x)==1:
        print("Yes")
    else:
        print("No")