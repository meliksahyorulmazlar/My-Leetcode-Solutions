class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        if n <2:
            return 0
        else:
            for i in range(2,n):
                if i == 2:
                    count += 1
                elif i % 2 == 0:
                    continue
                else:
                    is_prime = True
                    for j in range(3,n,2):
                        if i % j == 0 and i !=j:
                            is_prime = False
                    if is_prime:
                        count += 1
            return count

sol = Solution()
x = sol.countPrimes(100000)
print(x)
