class Solution(object):
    def generate(self, numRows):
        numbers=[]


        for i in range(numRows):
            items = []
            for j in range(i+1):
                top = self.factorial(i)
                bottom = self.factorial(j) * self.factorial(i-j)
                items.append(int(top/bottom))
            numbers.append(items)
        return numbers


    def factorial(self,n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n-1)


