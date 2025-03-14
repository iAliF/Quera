def game(number: int) -> int:
    return max(nums := tuple(int(x) for x in list(str(number)))) - min(nums)
