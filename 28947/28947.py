import random

haft_sin = [
    'sabze',
    'sib',
    'serke',
    'sir',
    'samanoo',
    'somaq',
    'senjed',
]

n = int(input())

for i in range(n):
    print(
        haft_sin.pop(
            random.randint(0, len(haft_sin) - 1)
        )
    )
