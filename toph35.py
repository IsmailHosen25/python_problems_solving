sum_of_numbers=int(input())
nums=list(map(int,input().split()))
s=0
for i in range(len(nums)):
      s=s+nums[i]
result=sum_of_numbers-s
print(result)
