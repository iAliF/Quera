n = int(input())

fib = [1, 1]

while fib[-1] <= n:
    fib.append(fib[-1] + fib[-2])

print("".join("+" if i in fib else "-" for i in range(1, n + 1)))
