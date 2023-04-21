n = int(input())
nums = [input() for _ in range(n)]
max_len = max(map(len, nums))

resp = {}

for step in range(1, max_len + 1):
    r = 0
    for num in nums:
        if len(num) >= step:
            r += int(num[-step])

    if len(resp) == step:
        r += resp[step - 1]

    if r < 10:
        resp[step - 1] = r
    else:
        resp[step - 1] = r % 10
        resp[step] = r // 10

print(''.join(map(str, reversed(resp.values()))))
