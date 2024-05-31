class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        prime_list = [True for i in range(n)]
        prime_list[0],prime_list[1] = False,False

        for i in range(2,int(n**0.5)+1):
            if prime_list[i] == True:
                for j in range(i*i,n,i):
                    prime_list[j] = False
        return sum(prime_list)

