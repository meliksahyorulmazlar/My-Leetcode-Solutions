class Solution(object):
    def countSeniors(self, details):
        count = 0
        for detail in details:
            tens = int(detail[11]) * 10
            ones = int(detail[12])
            age = tens+ones
            if age > 60:
                count +=1
        return count
