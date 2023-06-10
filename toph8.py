def fibonacci_numbers(n):
    x = 0
    y = 1
    if n < 0:
        return -1
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return y
    else:
        for i in range(1, n):
            z = x+y
            x = y
            y = z
        return y
n = int(input())
print(fibonacci_numbers(n))