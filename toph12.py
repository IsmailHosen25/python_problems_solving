import re
from collections import Counter
x = re.sub(r'[^\w\s]', '', input())
y = x.split()
p = x.lower().split()
print(y[p.index(max(p,key=len))])
print(y[p.index(min(p,key=len))])
print(y[p.index(Counter(p).most_common(1)[0][0])])




# str=list(input().split("."))
# str_m=list(str[0].split(" "))

# longest_word=str_m[0]
# for i in range(len(str_m)):
#     if(len(longest_word)<len(str_m[i])):
#         longest_word=str_m[i]
#     else:
#         continue
# sorted_word=str_m[0]
# for i in range(len(str_m)):
#     if(len(sorted_word)>len(str_m[i])):
#         sorted_word=str_m[i]
#     else:
#         continue
# print(longest_word,sorted_word, sep=" ")
    