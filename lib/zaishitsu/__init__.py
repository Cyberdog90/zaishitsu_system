from datetime import datetime

__all__ = ["now", "error"]


def now():
    now_time = datetime.now()
    return f"{now_time.year}/{now_time.month}/{now_time.day} " \
           f"{now_time.hour}:{now_time.minute}:{now_time.second}"


def error(message: str):
    with open("error.log", "a") as f:
        f.write(f"{now()}\t\t{message}\n")
