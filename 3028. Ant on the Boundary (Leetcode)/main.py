class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        location = 0
        count = 0
        for num in nums:
            if num >0:
                location += num
            elif num < 0:
                location += (num)

            if location == 0:
                count += 1

        return count