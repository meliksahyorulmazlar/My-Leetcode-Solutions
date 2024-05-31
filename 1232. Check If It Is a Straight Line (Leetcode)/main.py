class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]):
        gradients = []
        for i in range(0,len(coordinates)-1):
            y2 = coordinates[i+1][1]
            y1 = coordinates[i][1]
            x2 = coordinates[i+1][0]
            x1 = coordinates[i][0]
            try:
                gradient = (y2-y1)/(x2-x1)
            except ZeroDivisionError:
                if x2 == 0 and x1 ==0:
                    gradient= "undefined"
                else:
                    gradient = 0
            gradients.append(gradient)
            if i >= 1 and gradients.count(gradient) == 1:
                return False
        return True