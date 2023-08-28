from datetime import datetime, timedelta


def dt_from_string(string: str) -> datetime:
    return datetime.strptime(
        string,
        '%H:%M:%S'
    )


def delta_strftime(td: timedelta) -> str:
    mm, ss = divmod(td.seconds, 60)
    hh, mm = divmod(mm, 60)
    return "%02d:%02d:%02d" % (hh, mm, ss)


a, b = (
    dt_from_string(input())
    for _ in range(2)
)

delta: timedelta = b - a

if delta.total_seconds() != 0:
    print(delta_strftime(delta))
else:
    print('24:00:00')
