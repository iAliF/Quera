def get_time(hour: int, minute: int):
    hour = (12 - hour) % 12
    minute = (60 - minute) % 60
    return f"{hour:02d}:{minute:02d}"


if __name__ == '__main__':
    print(
        get_time(
            *(int(x) for x in input().split())
        )
    )
