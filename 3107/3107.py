x, y = [list(map(int, input().split())) for _ in range(2)]

if all(x[i] >= y[i] for i in range(2)):
    print("yes")
else:
    print("no")
