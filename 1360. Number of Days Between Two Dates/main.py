import datetime


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        if date1 > date2:
            c = date1
            date1 = date2
            date2 = c

        date1 = date1.split("-")
        year1 = int(date1[0])
        month1 = int(date1[1])
        day1 = int(date1[2])
        d1 = datetime.datetime(day=day1, month=month1, year=year1)

        date2 = date2.split("-")
        year2 = int(date2[0])
        month2 = int(date2[1])
        day2 = int(date2[2])
        d2 = datetime.datetime(day=day2, month=month2, year=year2)

        days = 0
        while d1 < d2:
            one_day = datetime.timedelta(days=1)
            d1 += one_day
            days += 1

        return days

