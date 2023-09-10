n, x, y = list(
    map(
        int,
        input().split(' ')
    )
)

if n % x == 0:
    print(n // x, 0)
elif n % y == 0:
    print(0, n // y)
else:
    xs = 0
    while xs < n:
        xs += x

        if (r := (n - xs)) % y == 0:
            print(xs // x, r // y)
            exit()

    print(-1)
