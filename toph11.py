pyramid_size = int(input())
x = 1

while pyramid_size > 0:
    if x > 1:
        print(" "*(pyramid_size-1)+("*" + " ")*(x-1)+("*"))
    else:
        print(" "*(pyramid_size-1)+"*")
    pyramid_size -= 1
    x += 1