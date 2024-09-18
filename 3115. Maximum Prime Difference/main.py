class Solution:
    def maximumPrimeDifference(self, nums: list[int]) -> int:
        numbers = [i for i in range(len(nums)) if self.prime(nums[i]) == True]

        if len(numbers) == 1:
            return 0
        else:
            return max(numbers) - min(numbers)

    def prime(self, number: int) -> bool:
        if number == 1:
            return False
        elif number == 2:
            return True
        elif number % 2 == 0:
            return False
        else:
            for i in range(3, int(number ** 0.5) + 1):
                if number % i == 0:
                    return False
            return True

