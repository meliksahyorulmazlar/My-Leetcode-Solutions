class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        distance = 0

        while mainTank >0:
            if mainTank >=5:
                if additionalTank >=1:
                    additionalTank -= 1
                    mainTank -= 4
                    distance += 50
                else:
                    mainTank -= 5
                    distance += 50
            else:
                distance += (mainTank)*10
                mainTank = 0
        return distance