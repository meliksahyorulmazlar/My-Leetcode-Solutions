class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        months = [0,3,2,5,0,3,5,1,4,6,2,4]
        if month < 3:
            year -= 1
        remainder = (year + year//4 -year//100 + year//400 + months[month-1]+day)%7
        days = {0:"Sunday",1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday"}
        return days[remainder]


