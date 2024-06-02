class Solution(object):
    def getRow(self, rowIndex):
        numbers =[]
        count = 0
        for i in range(rowIndex+1):
            top = (self.factorial(rowIndex))
            bottom = (self.factorial(i)) * (self.factorial(rowIndex-i))
            numbers.append(int(top/bottom))
        return numbers



    def factorial(self,n):
        if  n == 0 or n==1:
            return 1
        else:
            return n * self.factorial(n-1)


s = Solution()
s.getRow(3)
