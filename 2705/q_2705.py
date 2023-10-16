p, d = (int(x) for x in input().split())
n = d

while n % p > (p/2):
    n += d

print(n)