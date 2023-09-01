def func(loc: int, dest: int) -> str:
    dx = dest - loc

    if dx > 0:
        return dx * "R"
    elif dx == 0:
        return "Saal Noo Mobarak!"
    elif dx < 0:
        return (-dx) * "L"


if __name__ == '__main__':
    print(
        func(
            *(int(x) for x in input().split())
        )
    )
