class Solution(object):
    def maximumCount(self, nums):
        negative = 0
        positive = 0
        for num in nums:
            if num >0:
                positive += 1
            elif num < 0:
                negative += 1
        return max(negative,positive)