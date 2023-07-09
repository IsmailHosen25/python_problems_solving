n = int(input())
l = list(map(int,input().split()))
sorted_l = sorted(l)
if l == sorted_l:
    print('Yes')
else:
    print("No")