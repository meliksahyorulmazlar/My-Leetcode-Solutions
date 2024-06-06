class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        greatest = 0
        count = 0
        for num in nums:
            if num == 1:
                count +=1
                if count > greatest:
                    greatest = count
            else:
                count = 0
        return greatest