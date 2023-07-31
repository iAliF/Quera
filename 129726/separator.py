from typing import List, Tuple


def separator(ls) -> Tuple[List[int], List[int]]:
    new = (
        [],
        []
    )
    for x in ls:
        new[x % 2].append(x)

    return new
