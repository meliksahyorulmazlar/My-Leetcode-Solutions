class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        numbers = []
        for num in nums:
            if nums.count(num) == 1:
                numbers.append(num)
                if len(numbers) == 2:
                    return numbers