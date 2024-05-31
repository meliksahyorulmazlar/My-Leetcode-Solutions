class Solution:
    def diagonalPrime(self, nums: list[list[int]])->int:
        greatest_prime = 0
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                number = nums[i][j]
                if i == j or i+j == len(nums)-1:
                    if number > greatest_prime:
                        is_prime = True
                        if number < 2:
                            is_prime = False
                        elif number == 2:
                            is_prime = True
                            greatest_prime = 2
                        elif number %2 == 0:
                            is_prime = False
                        else:
                            for k in range(3,int(number**0.5)+1,2):
                                if number % k == 0:
                                    is_prime = False
                                    break
                            if is_prime:
                                greatest_prime = number
        return greatest_prime






