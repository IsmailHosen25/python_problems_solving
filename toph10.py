num=int(input())
factorial_r=1
for i in range(num,0,-1):
    factorial_r=factorial_r*i

if(factorial_r%10000==0):
    print("0000")
else:
    print(factorial_r%10000)
