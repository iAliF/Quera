n = int(input())

print(
    max(
        (
            len(
                set(input())
            )
            for _ in range(n)
        )
    )
)
