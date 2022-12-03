from day1 import resolve_day1
from day2 import resolve_day2
from day3 import resolve_day3

DAY = 0

def resolve_all():
    resolve_day1()
    resolve_day2()
    resolve_day3()


def resolve(day):
    if day == 0:
        resolve_all()
    if day == 1:
        resolve_day1()
    elif day == 2:
        resolve_day2()
    elif day == 3:
        resolve_day3()


if __name__ == '__main__':
    resolve(DAY)
