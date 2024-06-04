class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        numbers = []
        for num in nums:
            count = 0
            for n in nums:
                if num > n:
                    count +=1
            numbers.append(count)
        return numbers