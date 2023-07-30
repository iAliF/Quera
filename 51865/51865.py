grade, days = list(
    map(
        int,
        (input() for _ in range(2)))
)

if days == 0:
    grade = 20
elif days != 7:
    grade -= days

print(grade if grade > 0 else 0)
