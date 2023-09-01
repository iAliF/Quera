# Get numbers from input
nums = [
    int(input())
    for _ in range(6)
]

total = 0

for i in range(3):
    # Total += minimum of (a[i] + b[i])
    total += min(nums[2 * i:2 * (i + 1)])

print(total)
