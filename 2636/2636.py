count = (1, 1, 2, 2, 2, 8)
cinput = tuple(
    map(int, input().split(' '))
)

print(
    *(str(count[i] - cinput[i]) for i in range(6)),
    sep=" "
)
