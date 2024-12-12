class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        possible_sums = []
        power = 0
        while True:
            if pow(3,power) > n:
                break
            elif pow(3,power) == n:
                return True
            else:
                amount = pow(3,power)
                new_sums = []
                for item in possible_sums:
                    if item+amount == n:
                        return True
                    else:
                        new_sums.append(item+amount)
                new_sums.append(amount)
                for k in new_sums:
                    possible_sums.append(k)
                power +=1
        return False


sol = Solution()

x = sol.checkPowersOfThree(21)
print(x)



