n = int(input())

old = [1]

for i in range(1, n + 1):
    new = [1, 1] if i > 1 else [1]

    for x in range(2, i):
        new.insert(-1, old[x - 2] + old[x - 1])

    print(*new)
    old = new