"""
INPUT

n q l

dataset (n * l)
to search (q * l)
"""

n, q, l = (
    int(x)
    for x in input().split(' ')
)

dataset = {
    (x := input().split())[0]: x[1]
    for _ in range(n)
}

print(
    *(
        dataset.get(input(), 'Unknown')
        for _ in range(q)
    ),
    sep="\n"
)
