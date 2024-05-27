class Solution:
    def dayOfYear(self, date: str) -> int:
        year = int(date.split("-")[0])
        month = int(date.split("-")[1])
        day = int(date.split("-")[2])

        normal_year = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31,9: 30, 10: 31, 11: 30, 12: 31}
        leap_year = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        total_days = 0
        if year % 4 != 0:
            is_leap = False
        elif year % 4 == 0 and year % 400 == 0:
            is_leap = True
        elif year % 4 == 0 and year % 100 == 0:
            is_leap = False
        else:
            is_leap = True
        dates = None
        if is_leap:
            dates = leap_year
        else:
            dates = normal_year



        for i in range(1,month):
            total_days += dates[i]

        total_days += day
        return total_days
