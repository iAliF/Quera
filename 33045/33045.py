n = int(input())

nums = []
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            nums.append(j)

print(len(nums), sum(nums))
