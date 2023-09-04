from typing import List


def rotate(nums: List[int]):
    return [*nums[1:], nums[0]]


def func(chocs: str) -> str:
    chocs = [int(x) for x in chocs.split()]
    ate = [0, 0, 0, 0]

    i = 0
    while all(x > 0 for x in chocs):
        ate[i] += 1
        chocs[i] -= 1
        chocs = rotate(chocs)

        i = i + 1 if i < 3 else 0

    return ' '.join(map(str, ate))


if __name__ == '__main__':
    result = func(input())
    print(result)
