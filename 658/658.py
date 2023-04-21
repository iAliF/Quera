count = int(input())
nums = input().replace('−', '-')
nums = nums.split(',') if ',' in nums else nums.split(' ')
nums = list(map(int, nums))

profits = []

for step in range(0, count + 1):
    start = 1
    while (end := start + step) <= count:
        profits.append(sum(nums[start - 1:end]))
        start += 1

print(max(max(profits), 0))
