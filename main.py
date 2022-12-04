from datetime import datetime

from day1 import resolve_day1
from day2 import resolve_day2
from day3 import resolve_day3
from day4 import resolve_day4
from inputs.leaderboard import leaderboard

DAY = 0
LEADERBOARD = 1


def show_leaderboard():
    for member in leaderboard['members']:
        # print(leaderboard['members'][member])
        m = leaderboard['members'][member]
        print("__________________________")
        print(m["name"], "-", "Stars:", m["stars"], " Score:", m["local_score"])
        if len(m['completion_day_level']) > 0:
            for x in m['completion_day_level']:
                if "get_star_ts" in m['completion_day_level'][x]["1"] and "get_star_ts" in m['completion_day_level'][x]["2"]:
                    ts1 = int(m['completion_day_level'][x]["1"]["get_star_ts"])
                    ts2 = int(m['completion_day_level'][x]["2"]["get_star_ts"])

                    print("Day", x, datetime.utcfromtimestamp(ts1).strftime('%H:%M:%S'), datetime.utcfromtimestamp(ts2).strftime('%H:%M:%S'))



                # if "get_star_ts" in m['completion_day_level'][x]["2"]:
                #     ts = int(m['completion_day_level'][x]["2"]["get_star_ts"])
                #     print(datetime.utcfromtimestamp(ts).strftime('%H:%M:%S'))
    print("__________________________")
    print()
    print()

def resolve_all():
    resolve_day1()
    resolve_day2()
    resolve_day3()
    resolve_day4()


def resolve(day):
    if LEADERBOARD:
        show_leaderboard()
    if day == 0:
        resolve_all()
    if day == 1:
        resolve_day1()
    elif day == 2:
        resolve_day2()
    elif day == 3:
        resolve_day3()
    elif day == 4:
        resolve_day4()


if __name__ == '__main__':
    resolve(DAY)
