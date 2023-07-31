n = int(input().split(" ")[0])

print(
    sum(input().count("*") for _ in range(n))
)
