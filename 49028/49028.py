n = int(input())
changes = 0
last = input()

for _ in range(n - 1):
    if (inp := input()) != last:
        changes += 1
        last = inp

print(changes)
