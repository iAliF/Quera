xs = []
ys = []
for _ in range(3):
    a, b = map(int, input().split(' '))
    xs.append(a)
    ys.append(b)

xs = sorted(xs, key=lambda x: xs.count(x))
ys = sorted(ys, key=lambda y: ys.count(y))

print(xs[0], ys[0])
