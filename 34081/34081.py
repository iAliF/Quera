n, k = (int(x) for x in input().split())

x = 1
"""if (d := (n - x)) % k == 0:
    print(d // k)
    exit()"""

while (x := x + k) % n != 1:
    pass

print(x // k)
