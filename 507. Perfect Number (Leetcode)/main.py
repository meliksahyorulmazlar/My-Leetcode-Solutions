class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        factors = [1]
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                factors.append(i)
                factors.append(num//i)

        return sum(factors) == num