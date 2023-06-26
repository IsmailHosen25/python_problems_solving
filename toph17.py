lines = []
while True:
    try:
        line = input()
        lines.append(line)
    except EOFError:
        break

for line in lines[1:]:
    count = 0

    for char in line:
        if char in "123456O":
            count += 1

    overs = count // 6
    balls = count % 6

    if overs > 0:
        if overs > 1:
            print(overs, "OVERS", end=" ")
        else:
            print(overs, "OVER", end=" ")

    if balls > 0:
        if balls > 1:
            print(balls, "BALLS", end=" ")
        else:
            print(balls, "BALL", end=" ")

    print()