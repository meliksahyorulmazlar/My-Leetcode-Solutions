class Solution:
    def reformatDate(self, date: str) -> str:
        month_dictionary = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
        dates = date.split()
        year = dates[2]
        month = month_dictionary[dates[1]]
        day = int(dates[0].rstrip("th").rstrip("nd").rstrip("rd").rstrip("st"))
        if day < 10:
            day = f"0{day}"
        return f"{year}-{month}-{day}"
        





    

