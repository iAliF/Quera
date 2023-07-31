count, orig, user = (
    input() for _ in range(3)
)

print(
    sum(
        1 if orig[i] != user[i] else 0
        for i in range(int(count))
    )
)
