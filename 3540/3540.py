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
    xc = yc = 0
    while (xc * x + yc * y) < n:
        xc += 1

        if (r := (n - xc * x)) % y == 0:
            print(xc, r // y)
            exit()

print(-1)
