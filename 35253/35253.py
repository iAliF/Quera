n = int(input())
w = list(
    map(
        int,
        input().split(' ')
    )
)

wms = list(range(1, n + 1))

while len(wms) > 1:
    w1, w2 = wms[0:2]
    del wms[0 if w[w1 - 1] < w[w2 - 1] else 1]

print(wms[0])
