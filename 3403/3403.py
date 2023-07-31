nums = []
prod = 1

for _ in range(4):
    x = float(input())
    nums.append(x)
    prod *= x

msgs = {
    "Sum": sum(nums),
    "Average": sum(nums) / len(nums),
    "Product": prod,
    "MAX": max(nums),
    "MIN": min(nums)
}

for k, v in msgs.items():
    v = str(v)
    v += "0" * (6 - len(v.split(".")[-1]))
    print(f"{k} : {v}")
