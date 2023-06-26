n = float(input())

n2 = int(n)
x = int(n2/10)
print("[", end="")
for i in range(10):
    if ( i <= x-1) : print("+", end="")
    else: print(".", end="")

print("] ", end="")
print(n2, end="%")